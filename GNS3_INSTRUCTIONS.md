# GNS3 Instructions for OSPF Lab

This document provides step-by-step instructions on how to use the generated configuration files to set up an OSPF lab in GNS3.

## 1. Create a New GNS3 Project

1.  Open GNS3 and click on **File > New blank project**.
2.  Give your project a name (e.g., `OSPF_Lab`) and click **OK**.

## 2. Add Routers to the Topology

1.  In the **Routers** section of the **Devices Toolbar**, select a router model (e.g., `c7200`).
2.  Drag and drop two routers into the project workspace. GNS3 will automatically name them `R1` and `R2`.

## 3. Connect the Routers

1.  Click on the **Add a link** button in the toolbar.
2.  Click on `R1` and select the `GigabitEthernet0/0` interface.
3.  Click on `R2` and select the `GigabitEthernet0/0` interface.

## 4. Import the Generated Configuration Files

1.  Right-click on `R1` and select **Import/Export config**.
2.  Click on the **Import** button and select the `gns3_configs/R1_config.txt` file.
3.  Click **OK**.
4.  Repeat the same process for `R2`, selecting the `gns3_configs/R2_config.txt` file.

## 5. Start the Routers

1.  Click on the **Start/Resume all devices** button in the toolbar.

## 6. Open a Console to the Routers

1.  Right-click on `R1` and select **Console**.
2.  Right-click on `R2` and select **Console**.

## 7. Verify the OSPF Configuration

1.  In the console of `R1`, run the following command to check the OSPF neighbors:
    ```
    show ip ospf neighbor
    ```
    You should see `R2` in the output.

2.  In the console of `R2`, run the same command to check the OSPF neighbors:
    ```
    show ip ospf neighbor
    ```
    You should see `R1` in the output.

## 8. Use Wireshark to Capture and Analyze OSPF Packets

1.  Right-click on the link between `R1` and `R2` and select **Start capture**.
2.  Wireshark will open and start capturing packets on the link.
3.  You can filter for OSPF packets by typing `ospf` in the filter bar.
4.  You can now analyze the OSPF packets, such as Hello packets, Database Description (DBD) packets, and Link-State Update (LSU) packets.
