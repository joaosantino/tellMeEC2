import boto3

region_name = boto3.session.Session().region_name
ec2 = boto3.resource('ec2', region_name)


def get_instance_info() -> dict:
    for instance in ec2.instances.all():
        data = {
            "Instance ID": f"{instance.id}",
            "AMI ID": f"{instance.image_id}",
            "State": f"{instance.state['Name']}",
            "Priv. IP": f"{instance.private_ip_address}",
            "Pub. IP": f"{instance.public_ip_address}",
            "Priv. DNS": f"{instance.private_dns_name}",
            "Pub. DNS": f"{instance.public_dns_name}",
            "VPC ID": f"{instance.vpc_id}",
            "Subnet ID": f"{instance.subnet_id}",
            "Security Group": {}}

        sec_group = {}

        for i in range(len(instance.security_groups)):
            sec_group["SG Name"] = \
                f"{instance.security_groups[i]['GroupName']}"
            sec_group["SG ID"] = f"{instance.security_groups[i]['GroupId']}"

        data["Security Group"] = sec_group

    return data
