import visa
import numpy
import pyvisa
rm = visa.ResourceManager()
inst = rm.open_resource('TCPIP0::192.168.1.10::hpib7,16::INSTR')
print(inst.query('*IDN?'))


inst.query_ascii_values('CURV?')   # ascii码打印数据
inst.query_binary_values()



#读ASCII码数据
values = inst.query_ascii_values('CURV?', converter='x', separator='$')  # 得到数据列表
values = inst.query_ascii_values('CURV?', container=numpy.array)  # 其他数据类型定义

#读二进制数据
values = inst.query_binary_values('CURV?', datatype='d', is_big_endian=True)  # 设置大小端

# 写ASCII数据
values = list(range(100))  
inst.write_binary_values('WLISt:WAVeform:DATA somename,', values, converter = 'x', separater = '$') 
# converter可以是任何一种Python字符串类型。也可以自定义一个单字符表示的字符串类型。默认converter是‘f’。默认的间隔符是“,”。


# 写二进制数据
values = list(range(100))  
inst.write_binary_values('WLISt:WAVeform:DATA somename,', values)

# 调试代码
inst.write('CURV?')
data = inst.read_row()
data = inst.read.bytes(1)

# Resource类方法
# '''每个仪器都有一个特定的session头
# '''
# inst.session()
# inst.timeout()
#
# # pyvisa 读数据是一块一块的，每块默认大小是20kB，可以更改
# inst.chuck_size = 102400
#
# # 终止符
# '''
# 终止符可以是单个字符，也可以是字符的组合。当这个字符或这个字符组合出现在输入字符流，读操作将被终止，
# 读取的消息被传递给调用的应用。下一个读操作开始于输入字符流的上一个结束符。PyVISA提供终止符分离后的消息（数据）。
# 可以设置每个仪器的终止符。
# inst.read_termination = '\r'
# '\r'为换行符。
# 亦可以在创建仪器/设备对象时给出：
# my_instrument = rm.open_resource("GPIB::10", read_termination='\r')
# 默认的终止符取决于总线系统。对于GPIB，为空。对于RS232，为换行符。
# 可以设置终止符到输出信息中，并用write_termination参数通知设备。
# '''

inst.query("status:measurement?")  # 
inst.write("trace:clear; trace:feed:control next")
