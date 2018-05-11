import argparse
import time

from boto.ec2.connection import EC2Connection
from boto.ec2.regioninfo import *

EC2_ACCESS_KEY = '4426435fe0e349079237b578cef7db12'
EC2_SECRET_KEY = 'f6bf9966dc3847738c390461c6e8cd08'
DEFAULT_IMAGE_ID = 'ami-fe917e46'
DEFAULT_KEY_PAIR = 'Default-cloud'
DEFAULT_PLACE = 'melbourne-np'

conn = EC2Connection(aws_access_key_id=EC2_ACCESS_KEY,
                     aws_secret_access_key=EC2_SECRET_KEY,
                     is_secure=True,
                     region=RegionInfo(name="NeCTAR", endpoint="nova.rc.nectar.org.au"),
                     validate_certs=False,
                     port=8773,
                     path="/services/Cloud")


def create_instances(count=1):
    instance_list = []
    for c in range(count):
        instance_list.append(
            conn.run_instances(DEFAULT_IMAGE_ID,
                               key_name=DEFAULT_KEY_PAIR,
                               instance_type='m1.medium',
                               security_groups=['default','ssh','http','icmp','DB show','Frontend'],
                               placement=DEFAULT_PLACE)
        )

    return map(lambda x: x.instances[0], instance_list)


def get_all_instance_ids():
    return map(lambda x: x.instances[0].id, conn.get_all_instances())


def get_instance(instance_id):
    return conn.get_all_instances(instance_id)[0].instances[0]


def check_status(instance_id):
    print 'checking status of [%s]...' % instance_id
    return get_instance(instance_id).state


def wait_status(instance_id, status, max_loop=20):
    loop = 0

    while loop < max_loop:
        time.sleep(15)
        if check_status(instance_id) == status:
            return True
        loop += 1

    return False


def terminate_instance(instance_id):
    return get_instance(instance_id).terminate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=1, help='instance count')
    parser.add_argument('-o', type=str, help='start or terminate')
    args = parser.parse_args()

    if not args.o:
        parser.print_help()
        exit(1)

    if args.o.lower() == 'start':
        for ins in create_instances(args.n):
            if wait_status(ins.id, 'running'):
                instance = get_instance(ins.id)
                print instance.id, instance.ip_address, instance.state
            else:
                print 'create %s failed.' % ins.id

        for ins_id in get_all_instance_ids():
            vol_req = conn.create_volume(0.1, 'melbourne-np', '', 'melbourne')
            conn.attach_volume(vol_req.id, ins_id, '/dev/vdc')

    elif args.o.lower() == 'terminate':
        # Terminating all instances
        for ins_id in get_all_instance_ids():
            terminate_instance(ins_id)
    else:
        parser.print_help()





        