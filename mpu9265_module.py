import serial
import time
import re
import numpy as np
import math


def mpu92_65(data_sensor):
    #ser = serial.Serial('COM3', 9600)

    angle_x = 0
    angle_y = 0
    angle_z = 0
    Filter_gain = 0.05

    #while True:
    start = time.time()
    #    #print('thie is start:' + str(start))
    #    data_sensor = str(ser.readline())

    #print(data_sensor)
    data_sensor_modify = re.findall("[-0-9.]+", data_sensor)
    print('data_sensor_modify: ' + str(data_sensor_modify))

    #Gyroscope data
    data_gyro = data_sensor_modify[3:6]
    data_gyro_massive = np.array([float(data_gyro[0]), float(data_gyro[1]), float(data_gyro[2])])
    #print("Data_gyro_massive" + str(data_gyro_massive))

    #Accelerometer data
    data_accel = data_sensor_modify[0:3]
    data_accel_massive = np.array([float(data_accel[0]), float(data_accel[1]), float(data_accel[2])])

    #Magnetometer data
    data_mag = data_sensor_modify[6:9]
    data_mag_massive = np.array([float(data_mag[0]), float(data_mag[1]), float(data_mag[2])])

    end_time = time.time()
    integrate_time = end_time - start
    #print("Integrate time: " + str(integrate_time))
    GyX_angle = (data_gyro_massive[0] * (integrate_time)+angle_x)
    GyY_angle = (data_gyro_massive[1] * (integrate_time)+angle_y)
    GyZ_angle = (data_gyro_massive[2] * (integrate_time)+angle_z)

    AcZ_angle = np.rad2deg(math.atan(data_accel_massive[2]/ (math.sqrt(data_accel_massive[1] * data_accel_massive[1] + data_accel_massive[0] * data_accel_massive[0])))) #* (float)rad2degree
    AcY_angle = np.rad2deg(-math.atan(data_accel_massive[1]/ (math.sqrt(data_accel_massive[0] * data_accel_massive[0] + data_accel_massive[2] * data_accel_massive[2])))) #* (float)rad2degree
    AcX_angle = np.rad2deg(math.atan(data_accel_massive[0]/ (math.sqrt(data_accel_massive[1] * data_accel_massive[1] + data_accel_massive[2] * data_accel_massive[2])))) #* (float)rad2degree

    angle_x = Filter_gain * GyX_angle + (1 - Filter_gain) * AcX_angle
    angle_y = Filter_gain * GyY_angle + (1 - Filter_gain) * AcY_angle
    angle_z = Filter_gain * GyZ_angle + (1 - Filter_gain) * AcZ_angle

    mag_calibration_matrix = [[14.773701, 0.182207, -0.392104],
                             [0.182207, 15.647909, -0.120855],
                             [-0.392104, -0.120855, 13.817847]]
    bias = [15.641216, 50.000813, -16.682523]
    def get_calibrated(data_mag_massive, bias, mag_calibration_matrix):
        uncalibrated_values = [data_mag_massive[0] - bias[0], data_mag_massive[1] - bias[1], data_mag_massive[2] - bias[2]]
        calibrated_values = [0, 0, 0]
        for i in range(0, 3):
            for j in range(0, 3):
                calibrated_values[i] += mag_calibration_matrix[i][j] * uncalibrated_values[j]
        return {'x': calibrated_values[0],
                'y': calibrated_values[1],
                'z': calibrated_values[2]}
    def heading(get_calibrated, Ax, Ay):
        data = get_calibrated(data_mag_massive, bias, mag_calibration_matrix)
        Ax = Ax * math.pi / 180
        Ay = Ay * math.pi / 180
        Mx = [[1.0, 0.0, 0.0],
              [0.0, math.cos(Ax), -math.sin(Ax)],
              [0.0, math.sin(Ax), math.cos(Ax)]]
        My = [[math.cos(Ay), 0.0, math.sin(Ay)],
              [0.0, 1.0, 0.0],
              [-math.sin(Ay), 0.0, math.cos(Ay)]]
        # Vector rotation
        values = [data['x'], data['y'], data['z']]
        DATA = [0, 0, 0]
        for i in range(0, 3):
            for j in range(0, 3):
                DATA[i] += Mx[i][j] * values[j]
        values = [DATA[0], DATA[1], DATA[2]]
        DATA = [0, 0, 0]
        for i in range(0, 3):
            for j in range(0, 3):
                DATA[i] += My[i][j] * values[j]
        radians = -math.atan2(DATA[1], DATA[0])
        # Convert to degrees from radians
        return math.degrees(radians)
    #GyX_angle = (data_gyro_massive[0] * (integrate_time) + angle_x)
    result123 = heading(get_calibrated, Ax=0, Ay=0)

    #return("Angle " + str(n) + ":")
    return("Angle X: " + str(angle_x) + "\n"+"Angle Y: " + str(angle_y) + "\n"+"Angle Z accel + gyro: " + str(angle_z)
           + "\n"+"Angle Z mag: " + str(result123))