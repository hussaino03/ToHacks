
<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br>
<div align="center">
 <a href="https://github.com/hussaino03/ToHacks"> ![image](https://user-images.githubusercontent.com/49975886/170870224-e7314059-584b-46d1-9971-a9da66893d69.png) </a>
</a>
  <h1 align="center">ToHacks</h1>

  <p align="center">
   TBA
    <br>
    <br>
    <a href="https://github.com/hussaino03/ToHacks"><strong>Explore the docs »</strong></a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <br>
  <br>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## Snapshots of Approach

TBA

## Inspiration

In today's fast paced world there is hardly any time for people on the road to observe the surroundings and help the needy. However, the technology has successfully advanced well that the blind need not depend on any other person to perform their day to day activities. Guide Mobile is similar to that of a guide dog but it will help you to experience the scenery before you as if someone speaks with you.

## What it does

Guide Mobile which is a web app takes an image as input, and it provides a speech as an output where the sentence is generated with an image captioning algorithm.

## How We built it
The image captioning model was built with tensorflow library. The model was trained on the flick8k image captioning dataset. The overall accuracy of the model was around 80%. There was extensive data preprocessing for the images as well as the corresponding text data and there was use of both Convolutional and Sequential networks. We are deploying the model on web app with Django MVT.

## Challenges we ran into
The dataset provided with very limited images hence the output is not accurate for all the real world scenarios. Backend development was something new which under the limited time was challenging to build.

## Accomplishments that we're proud of
We were able to deploy the web app and test it successfully on images. The outputs for most of the cases yielded fruitful results.

## What we learned
Learned to maintain ML models and deploy them. Also learned to version the progress and develop robust backend for the website.

## What's next for Guide Mobile
Adding more features for the blind such as adding regional languages, networking etc. Also work on real time scenery description so they don't need to click a picture to understand.
### Features:
* Easy to interact UI
* Easy to understand voice
* Upcoming range for multiple languages

### Built With

* Python
* Django
* Tensorflow

<!-- GETTING STARTED -->
# Getting Started

<!-- PREREQUISITES -->
## Prerequisites
* Install the dependencies which are related to ML and Django
* Host the Django web application
* Input an image


## Installation
* perform ``` pip install -r requirements.txt```
* TBA

## Available Scripts

TBA

<!-- ROADMAP -->
## Roadmap

* [✅] Train an Image captioning model
* [✅] Test the model on few input images
* [✅] Design a Django app to deploy the model

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [GitHub README.md template](https://github.com/othneildrew/Best-README-Template)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hussaino03/ToHacks?color=%23&style=for-the-badge
[contributors-url]: https://github.com/hussaino03/ToHacks/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/hussaino03/ToHacks?style=for-the-badge
[issues-url]: https://github.com/hussaino03/ToHacks/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/hussaino03/ToHacks/blob/main/LICENSE.txt
[product-screenshot]: loginpage.png
