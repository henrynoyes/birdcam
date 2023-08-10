# BirdCam <img style='float: left;' src='https://drive.google.com/uc?id=1dFgM8Zmv-eSkuOC-TxIaG9cv4w5vL2-v' width='40'>
A birdhouse camera livestream with motion detection and mobile push notifications.

## Installing Pushover

1. Download the [Pushover App](https://apps.apple.com/us/app/pushover-notifications/id506088175?ls=1) from the app store.
2. Log in using my credentials
3.  Name your device, i.e. *henry-phone*
4. Await the notifications!

<img src='https://drive.google.com/uc?id=1KowDFC9tDI3PRVaZDQq4xBQpdLfR7E1P' width='360'>

## Lightweight Motion Detection

In order to comply with the weak compute power of the raspberry pi, the motion detection is triggered by a simple subtraction of consecutive frames as shown below. The mean difference in pixels triggers the motion threshold.

<img src='https://drive.google.com/uc?id=1Rm8x0Dx-g5Gqfwjv6Ee214PozlqjITzI'>

## RTSP Stream with MediaMTX
As of 6/6 the streaming service has been transferred from flask deployment to a local RTSP stream. This is done using [MediaMTX](https://github.com/bluenviron/mediamtx). Similar to the flask deployment, this allows for viewing using VLC and HTTP (web browser).

This decision was made as the motion detection has served its purpose in the early stages of birdcam activity. With a full family now in the house, there is less need for detection and an emphasis on consistent low-latency streaming, which MediaMTX provides.

## RTSP Stream with VLC

6/25 - Replaced MediaMTX service with libcamera + VLC implementaion. See [stream.sh](https://github.com/henrynoyes/birdcam/blob/master/stream.sh) for RTSP streaming command.

<details>

<summary><h2>Chapter 1: The Bluebirds</h2></summary>

## Update 5/24

The birdcam has its first visitor. Caught perfectly by the motion detection :D

<img src='https://drive.google.com/uc?id=1JxdaX_b2agvrhhAthUUC30HbFqnLgkEC' width='480'>

## Update 5/27

Sneak peek of nest construction

<img src='https://drive.google.com/uc?id=1c3bgAON2u6wkMhPySyEvu4j8OZperG_k' width='480'>

## Update 6/6

Eggcellent news, we are housing a [bluebird](https://en.wikipedia.org/wiki/Eastern_bluebird) family

<img src='https://drive.google.com/uc?id1NFYno0DHKJ6hqZvM1gG3PCixGheck87t' width='480'>

## Update 6/18

The babies have escaped their eggs

<img src='https://drive.google.com/uc?id=1qSHHHS8W3Xfd6uUDFyGrbL4U7G0LACnp' width='480'>

## Update 6/20

More baby action + mini afros

<img src='https://drive.google.com/uc?id=1oYa6HIhPoNQfa6uQmBUgdL28V9fWwivj' width='480'>

## Update 6/25

They are growing up fast and attempting to open their eyes

<img src='https://drive.google.com/uc?id=1IFQ6CcBKyjykmnkZCVVUbxHda5cuElMw' width='480'>

## Update 7/1

Full family of feathers

<img src='https://drive.google.com/uc?id=1erwKCLP9Vq_UHgjTe14k_EGrxgfg063T' width='480'>

## Update 7/5 

4 of the babies have officially left the nest! Only a single runt remains with mama...

<img src='https://drive.google.com/uc?id=1qqz9y7Km2aQdGe2dUMtYUFx6DbfmL-C6' width='480'> 

## Update 7/6

Success!! All the fledglings are flying out in the backyard

<img src='https://drive.google.com/uc?id=1os5mlrKsCxRTDXHyY9ZOBj1z8TAYSEdN' width='480'> 

Until the next family arrives...

</details>

<details>

<summary><h2>Chapter 2: The Wrens</h2></summary>

## Update 7/19

The bluebird nest was cleared out and a female [carolina wren](https://en.wikipedia.org/wiki/Carolina_wren) is our newest inhabitant. The four eggs were laid a few days ago and will take another week or so to hatch.

<img src='https://drive.google.com/uc?id=1FIE17XONfbawdHj5aQknFgtRs7dV2zmE' width='480'>

## Update 8/10

Some shots of the three baby wrens. Unfortunately one of the eggs did not hatch. The trio is fledging quickly!

<img src='https://drive.google.com/uc?id=1JWcTD1cm2bn5fweh-ir46sJz_dhYH022' width='480'>


</details>

