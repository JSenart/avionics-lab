# Avionics Lab Guide

## Introduction

In this Laboratory we will be working with `Software Defined Radio` (SDR). You have been assigned a work station in the room and a SDR kit with everything you need. Before proceeding please verify the package is complete:

|     |     |     |     |
| --- | --- | --- | --- |
| NESDR SMArt Series | <img src="figures/nesdr_smart.jpg" alt="Image Description" style="width:200px;">  | USB Extension | <img src="figures/extension.jpg" alt="Image Description" style="width:200px;">|
| Antena's Base | <img src="figures/antena_base.jpg" alt="Image Description" style="width:200px">  | Antena Kit | <img src="figures/antenas.jpg" alt="Image Description" style="width:200px;">|

It the coming sessions we will be working with this kit, alongside `SDRAngel` software and `MatLab` to capture and interpert radio comunications emited by Lisbon's Humberto Delgado Airport.
Once you have verified that no items are missing from your kit, head over to your work station so we can set it up with the required software.

### SDRAngel Setup
To get the software, just head over to the [download page](https://github.com/f4exb/sdrangel/releases). You'll find several downloadable assets of which you should choose the one with the `.tar.gz` extension as you are working on an Ubunto Linux distribution. SDRAngel developers have provided detailed descritpion on how to install the software [here](https://github.com/f4exb/sdrangel/wiki/Compile-from-source-in-Linux)

Go to the terminal and type the command
```bash
$picha coco
```
> **Warning:** This is an important warning message. Pay attention to this!

### NESDR SMART driver 
Before we can open SDRAngel, we have to download the driver for the NESDR in [download page](https://www.nooelec.com/store/qs). There you can find instructions on how to install.

### SDRAngel Innitialization

After setting up both the software and drivers, you can open the SDRAngel program.

At first, it will look like this:

 <img src="figures/SDRAngel_first.jpg" alt="Image Description" style="width:1000px;">


 First, you need to create a workspace. Press the workspaces button on the top left and then new on the drop down window:



<img src="figures/SDRAngel_workspace.jpg" alt="Image Description" style="width:1000px;">

Then, you can press the receiver button to look for your device:


<img src="figures/SDRAngel_receiver.jpg" alt="Image Description" style="width:40px;">

Here you will choose a receiving device. Choose the RTL-SDR device:


<img src="figures/SDRAngel_device.jpg" alt="Image Description" style="width:400px;">

The window will look like this. You will add a channel to the receiver that will process samples in the bandwidth of the receiver that depends on device sample rate and decimation. Press the button to add channels.

<img src="figures/SDRAngel_channels.jpg" alt="Image Description" style="width:800px;">


This opens the dialog where you can select which channel(s) to add. You can add more than one channel from this dialog by clicking Apply after each (or same) selection. In this example we will select "AM Demodulator" from the drpop down list. After this, press the play button on the top left window:


<img src="figures/SDRAngel_listening.jpg" alt="Image Description" style="width:1000px;">

You are now ready to start listening to signals. Note that your setup will be saved and restored across program stop/start cycles as the default configuration. If you want to restart from scratch you have to specify the --scratch option on the command line. You can also save different configurations by opening a dialog from the Preferences / Configuration menu.


### SDRAngel Channel Control

Gain - With this slider, you can adjust the gain to adapt to strong or weak signal. It is a measure of how much the amplitude of the signal will be increased or decreased.

<img src="figures/SDRAngel_gain.jpg" alt="Image Description" style="width:700px;">

Sample rate (SR) - This is the device sample rate divided by the decimation factor. The sample rate refers to the number of samples per second that the device can process or capture. The sample rate determines how finely the radio frequency (RF) spectrum is divided into discrete samples. A higher sample rate means more samples are taken per second, allowing for a more detailed representation of the RF signal. However, it also requires more computational resources and places higher demands on storage and data transfer.

<img src="figures/SDRAngel_SR.jpg" alt="Image Description" style="width:700px;">

Center Frequency - This term refers to the specific frequency around which the software tunes or operates the receiver or transmitter. You should change this value to the provided for each different signal you want to listen to.

<img src="figures/SDRAngel_center.jpg" alt="Image Description" style="width:700px;">

Frequency offset - The center frequency has a precision of kHz. This means that if you want to change the frequency in the hundreds of Hz, you will need to add or subtract with the offset option. Note that this is limited to the range of the bandwidth.

<img src="figures/SDRAngel_freq_offset.jpg" alt="Image Description" style="width:700px;">


Squelch - This option helps eliminate unwanted noise or weak signals when receiving radio communications. It is designed to silence the audio output when the received signal falls below a certain threshold.

<img src="figures/SDRAngel_squelch.jpg" alt="Image Description" style="width:700px;">



## Listening to the COM Channel

To begin getting acquainted with `SDRAngel` we will start by listening to the COM channel.


## Step 3: Title of Step 3

Explanation and instructions for completing Step 3.

- First, do this.
- Then, do that.
- Finally, complete the task.

## Conclusion

Summarize the guide and provide any final thoughts or additional resources.

For more information, refer to the [official documentation](https://example.com).
