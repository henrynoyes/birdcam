# BirdCam <img style='float: left;' src='https://doc-0g-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/1bk9tkp7ch3d0l3eul6gshr5rjvonjq7/1691701950000/14624311459661267869/*/1dFgM8Zmv-eSkuOC-TxIaG9cv4w5vL2-v?e=view&uuid=f82027cb-1e4d-4e8a-a579-d9c6fde8db81' width='40'>
A birdhouse camera livestream with motion detection and mobile push notifications.

## Installing Pushover

1. Download the [Pushover App](https://apps.apple.com/us/app/pushover-notifications/id506088175?ls=1) from the app store.
2. Log in using my credentials
3.  Name your device, i.e. *henry-phone*
4. Await the notifications!

<img src='https://doc-0g-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ort7plvb55tko0jprd692jfpekjcjkct/1691701950000/14624311459661267869/*/1KowDFC9tDI3PRVaZDQq4xBQpdLfR7E1P?e=view&uuid=f1a8eb2d-e73b-47bb-995a-84442f72d095' width='360'>

## Lightweight Motion Detection

In order to comply with the weak compute power of the raspberry pi, the motion detection is triggered by a simple subtraction of consecutive frames as shown below. The mean difference in pixels triggers the motion threshold.

<img src='https://doc-0c-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/a4h6lq9e7t75g4lt1tg62fu32c84vjnj/1691701950000/14624311459661267869/*/1Rm8x0Dx-g5Gqfwjv6Ee214PozlqjITzI?e=view&uuid=6253c515-b409-4cd5-8064-d20ec1482835'>

## RTSP Stream with MediaMTX
As of 6/6 the streaming service has been transferred from flask deployment to a local RTSP stream. This is done using [MediaMTX](https://github.com/bluenviron/mediamtx). Similar to the flask deployment, this allows for viewing using VLC and HTTP (web browser).

This decision was made as the motion detection has served its purpose in the early stages of birdcam activity. With a full family now in the house, there is less need for detection and an emphasis on consistent low-latency streaming, which MediaMTX provides.

## RTSP Stream with VLC

6/25 - Replaced MediaMTX service with libcamera + VLC implementaion. See [stream.sh](https://github.com/henrynoyes/birdcam/blob/master/stream.sh) for RTSP streaming command.

<details>

<summary><h2>Chapter 1: The Bluebirds</h2></summary>

## Update 5/24

The birdcam has its first visitor. Caught perfectly by the motion detection :D

<img src='https://doc-08-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/99kqiir9r1e8egbu6obb31qmstbvl3ku/1691701875000/14624311459661267869/*/1JxdaX_b2agvrhhAthUUC30HbFqnLgkEC?e=view&uuid=2a2577ec-7491-45af-95d6-5636b319a8e1' width='480'>

## Update 5/27

Sneak peek of nest construction

<img src='https://doc-04-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/1ml5cs75b5n4fsqtqv9vumohqcl0gp6h/1691701875000/14624311459661267869/*/1c3bgAON2u6wkMhPySyEvu4j8OZperG_k?e=view&uuid=6113209f-911c-4147-b347-ef28403c252c' width='480'>

## Update 6/6

Eggcellent news, we are housing a [bluebird](https://en.wikipedia.org/wiki/Eastern_bluebird) family

<img src='https://doc-04-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/uip1gukt3pscj0fibf1f6u9cev4boqn3/1691701875000/14624311459661267869/*/1NFYno0DHKJ6hqZvM1gG3PCixGheck87t?e=view&uuid=230c23d3-fbb3-4e33-b32c-88f323ade80c' width='480'>

## Update 6/18

The babies have escaped their eggs

<img src='https://doc-00-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/sfgre2r8ib9qc14fpf6r6kvrespsqs6v/1691701800000/14624311459661267869/*/1qSHHHS8W3Xfd6uUDFyGrbL4U7G0LACnp?e=view&uuid=c69235a8-9465-488d-87f1-0cf6917e2210' width='480'>

## Update 6/20

More baby action + mini afros

<img src='https://doc-0g-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/48jhp2ggalgvcsnqjhpjdlekno9ro0s7/1691701800000/14624311459661267869/*/1oYa6HIhPoNQfa6uQmBUgdL28V9fWwivj?e=view&uuid=6a8a66c9-0348-4703-a0ff-716c11357d55' width='480'>

## Update 6/25

They are growing up fast and attempting to open their eyes

<img src='https://doc-08-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/p4sp0oqu8d2f3ffmirctu501g19of6se/1691701800000/14624311459661267869/*/1IFQ6CcBKyjykmnkZCVVUbxHda5cuElMw?e=view&uuid=89403fd0-8984-455b-8d57-7f43f0933c9e' width='480'>

## Update 7/1

Full family of feathers

<img src='https://doc-14-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ihts3i2tpm6plrctpko5jud20oljg3ta/1691701800000/14624311459661267869/*/1erwKCLP9Vq_UHgjTe14k_EGrxgfg063T?e=view&uuid=1138a1f0-c54f-4e74-9458-54b6b7c76e48' width='480'>

## Update 7/5 

4 of the babies have officially left the nest! Only a single runt remains with mama...

<img src='https://doc-04-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/rue9jacpto21cv3j14f6nhta8ch0627n/1691701800000/14624311459661267869/*/1qqz9y7Km2aQdGe2dUMtYUFx6DbfmL-C6?e=view&uuid=b58a2f70-c849-400e-84b2-2ccdaa21a89d' width='480'> 

## Update 7/6

Success!! All the fledglings are flying out in the backyard

<img src='https://doc-08-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/rduj7kjtrhje48mh98570579m5108fnr/1691701350000/14624311459661267869/*/1os5mlrKsCxRTDXHyY9ZOBj1z8TAYSEdN?e=view&uuid=ede2d73f-55ae-485f-8b47-f2ce3cc9986f' width='480'> 

Until the next family arrives...

</details>

<details>

<summary><h2>Chapter 2: The Wrens</h2></summary>

## Update 7/19

The bluebird nest was cleared out and a female [carolina wren](https://en.wikipedia.org/wiki/Carolina_wren) is our newest inhabitant. The four eggs were laid a few days ago and will take another week or so to hatch.

<img src='https://doc-04-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/9l0fumegr1cr2crg4in1tivedrop1akr/1691701350000/14624311459661267869/*/1FIE17XONfbawdHj5aQknFgtRs7dV2zmE?uuid=6f335d3e-5a38-44f2-bd24-5ee94239f5b8' width='480'>

## Update 8/10

Some shots of the three baby wrens. Unfortunately one of the eggs did not hatch. The trio is fledging quickly!

<img src='https://doc-0c-bg-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/4hofees9bnt3mbn3jlk9f1asm8s69qib/1691701275000/14624311459661267869/*/1JWcTD1cm2bn5fweh-ir46sJz_dhYH022?e=view&uuid=e04d4848-6e5a-4ed4-adca-c3141c0cc165' width='480'>


</details>

