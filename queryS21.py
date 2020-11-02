import visa
import numpy
import pyvisa

rm = pyvisa.ResourceManager()
inst = rm.open_resource('TCPIP0::192.168.1.10::hpib7,16::INSTR')
print(inst.query('*IDN?'))

inst.write("*rst; status:preset; *cls")

numPoints = 10**4
start = 10**4
end = 10**8
inst.write('*CLS;*wai')
inst.write('CALCulate:PARameter:DEFine MySMeaS21, S21')
inst.write('DISPlay:WINDow1:STATE ON')
inst.write('DISPlay:WINDow1:TRACe1:FEED ''MySMeaS21''')
inst.write('DISPlay:WINDow1:TITLe:STATe ON')
inst.write('DISPlay:ANNotation:FREQuency ON')
inst.write('DISPlay:WINDow1:TRACe1:STATe ON')
inst.write('SENSe:SWEep:POINts %s',numPoints)
inst.write('SENSe:FREQuency:STARt %sHz',start)
inst.write('SENSe:FREQuency:STOP %sHz',end)
inst.write('TRIG:SOUR MANual')
inst.write('TRIG:SCOPe ALL')
inst.write('SENSe:SWEep:MODE CONTinuous')
inst.write('FORMat:DATA REAL,64')
inst.write('CALCulate:PARameter:SELect ''MySMeaS21''')


inst.write('INITiate:IMMediate;*wai')
inst.write('Display:WINDow1:TRACe1:Y:Scale:AUTO')
inst.write('CALCulate:DATA? SDATA')
inst.write("trace:feed sense1; trace:feed:control next")
inst.write("initiate")
inst.assert_trigger()
inst.wait_for_srq()
aa = inst.query_ascii_values("trace:data?")
print(aa)
inst.query("status:measurement?")
inst.write("trace:clear; trace:feed:control next")
"""
% fprintf(instrObj, 'FORMat:DATA REAL,64'); % 64  位 浮点数
fprintf(instrObj, 'FORMat:DATA ASCII'); % 编码方式
fprintf(instrObj, 'CALCulate:PARameter:SELect ''MySMeaS21''');
% i = 0;
% while (i < 2) % 多次读取的话使用循环即可
    fprintf(instrObj, 'INITiate:IMMediate;*wai');
fprintf(instrObj, 'Display:WINDow1:TRACe1:Y:Scale:AUTO');
fprintf(instrObj, 'CALCulate:DATA? SDATA');
% rawDataDB = binblockread(instrObj, 'double');
data = fread(instrObj); % 读取数据
fid = fopen('test.txt', 'wb');
data = fwrite(fid, data, 'char'); % 保存下来
% read terminating character
% d = fread(instrObj, 1, 'char');
% i = i + 1;
% end
"""
inst.close()
del inst

"""
instrumentVISAAddress = 'TCPIP0::192.168.1.10::hpib7,16::INSTR';
% Define frequency range
frequencyRange = [f1 f2]; % 起始频率
% Number of points in measurement
numPoints = NN;

instrObj = visa('agilent', instrumentVISAAddress); % 创立链接。
instrObj.InputBufferSize = 10e6; % set buffer
instrObj.ByteOrder = 'littleEndian';
fopen(instrObj);
clrdevice(instrObj); % clear
% Display information about instrument
IDNString = query(instrObj, '*IDN?'); % 信息查询
fprintf('Connected to: %s\n', IDNString);
% fprintf(instrObj, 'SYSTem:PREset');
% fprintf(instrObj, 'SYSTem:FPReset');
fprintf(instrObj, '*CLS;*wai');

% Define a measurement name and parameter
fprintf(instrObj, 'CALCulate:PARameter:DEFine ''MySMeaS21'',S21'); % s21
% Create a new display window and turn it on
fprintf(instrObj, 'DISPlay:WINDow1:STATE ON');
% Associate the measurements to WINDow1
fprintf(instrObj, 'DISPlay:WINDow1:TRACe1:FEED ''MySMeaS21''');
% Turn ON the Title, Frequency, and Trace Annotation to allow for
% visualization of the measurements on the instrument display
fprintf(instrObj, 'DISPlay:WINDow1:TITLe:STATe ON');
fprintf(instrObj, 'DISPlay:ANNotation:FREQuency ON');
fprintf(instrObj, 'DISPlay:WINDow1:TRACe1:STATe ON');

% Set the number of points
fprintf(instrObj, sprintf('SENSe:SWEep:POINts %s', num2str(numPoints)));
% Set the frequency ranges
fprintf(instrObj, sprintf('SENSe:FREQuency:STARt %sHz', num2str(frequencyRange(1))));
fprintf(instrObj, sprintf('SENSe:FREQuency:STOP %sHz', num2str(frequencyRange(2))));
fprintf(instrObj, 'TRIG:SOUR MANual'); % 手动触发
fprintf(instrObj, 'TRIG:SCOPe ALL');
fprintf(instrObj, 'SENSe:SWEep:MODE CONTinuous');
% Set  instrument to return the data back using binblock format
% fprintf(instrObj, 'FORMat:DATA REAL,64'); % 64  位 浮点数
fprintf(instrObj, 'FORMat:DATA ASCII'); % 编码方式
fprintf(instrObj, 'CALCulate:PARameter:SELect ''MySMeaS21''');
% i = 0;
% while (i < 2) % 多次读取的话使用循环即可
    fprintf(instrObj, 'INITiate:IMMediate;*wai');
fprintf(instrObj, 'Display:WINDow1:TRACe1:Y:Scale:AUTO');
fprintf(instrObj, 'CALCulate:DATA? SDATA');
% rawDataDB = binblockread(instrObj, 'double');
data = fread(instrObj); % 读取数据
fid = fopen('test.txt', 'wb');
data = fwrite(fid, data, 'char'); % 保存下来
% read terminating character
% d = fread(instrObj, 1, 'char');
% i = i + 1;
% end

% Close, delete, and clear instrument connections.
fclose(instrObj);
delete(instrObj);
clear
instrObj;
"""