
{
    "routers": [
        {
            "name": "R1",
            "interfaces": [
                {
                    "name": "GigabitEthernet0/0",
                    "ip_address": "10.0.0.1",
                    "subnet_mask": "255.255.255.252"
                }
            ]
        },
        {
            "name": "R2",
            "interfaces": [
                {
                    "name": "GigabitEthernet0/0",
                    "ip_address": "10.0.0.2",
                    "subnet_mask": "255.255.255.252"
                }
            ]
        }
    ],
    "links": [
        {
            "device1": "R1",
            "interface1": "GigabitEthernet0/0",
            "device2": "R2",
            "interface2": "GigabitEthernet0/0"
        }
    ]
}
