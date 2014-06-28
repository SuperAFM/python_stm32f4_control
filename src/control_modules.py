import commands
import string

motor_help='dd'
pid_help='ff'

def cmd_preprocess(cmd_param):
        c=cmd_param.split()
        if len(c)==2:
            return c[0],string.atoi(c[1])
        elif len(c)==1:
            return c[0],0
        else:
            return 'error',0        

def motor_control(cmds):
    if(len(cmds)==0):
        print motor_help;
    else:
        for cmd in cmds:
            k,v=cmd_preprocess(cmd)
            if k=='approach' or k=='ap':
                commands.cmd_execute('CMD_MOTOR','APPROACH',v)
            elif k=='withdraw' or k=='wd':
                commands.cmd_execute('CMD_MOTOR','WIDTHDRAW',v)
            elif k=='setorigin' or k=='so':
                commands.cmd_execute('CMD_MOTOR','SET_ORIGIN',v)
            elif k=='backtoorigin' or k=='bo':
                commands.cmd_execute('CMD_MOTOR','BACK_TO_ORIGIN',0)
            elif k=='autoapproach' or k=='aa':
                commands.cmd_execute('CMD_MOTOR','AUTO_APPROACH',0)
            elif k=='autowithdraw' or k=='aw':
                commands.cmd_execute('CMD_MOTOR','AUTO_WITHDRAW',0)
            elif k=='stop' or k=='st':
                commands.cmd_execute('CMD_MOTOR','STOP',0)
            else:
                print 'bad command %s' %(k)

def pid_control(cmds):
    if(len(cmds)==0):
        print pid_help;
    else:
        for cmd in cmds:
            k,v=cmd_preprocess(cmd)
            if k=='setp' or k=='sp':
                commands.cmd_execute('CMD_PID','SET_P',v)
            elif k=='seti' or k=='si':
                commands.cmd_execute('CMD_PID','SET_I',v)
            elif k=='setd' or k=='sd':
                commands.cmd_execute('CMD_PID','SET_D',v)
            elif k=='delay' or k=='de':
                commands.cmd_execute('CMD_PID','SETPOINT',v)        
            elif k=='enable' or k=='en':
                commands.cmd_execute('CMD_PID','ENABLE',0)
            else:
                print 'bad command %s' %(k)

def dds_control(cmds):
    return
def scan_control(cmds):
    return
def help():
    pass

control_funcs={'scan':scan_control,'dds':dds_control,'pid':pid_control,'motor':motor_control,'help':help}