
# Immothep

<!-- PROJECT LOGO -->
<style>
    .cat {
    left: 50%;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    margin:-60px 0 0 -60px;
    -webkit-animation:spin 4s linear infinite;
    -moz-animation:spin 4s linear infinite;
    animation:spin 4s linear infinite;
    }
    @-moz-keyframes spin { 100% { -moz-transform: rotate(360deg); } }
    @-webkit-keyframes spin { 100% { -webkit-transform: rotate(360deg); } }
    @keyframes spin { 100% { -webkit-transform: rotate(360deg); transform:rotate(360deg); } }
</style>

<div class='cat'>
	<img class="image" src="http://makeameme.org/media/templates/120/grumpy_cat.jpg" alt="" width="120" height="120">
</div>

<br />
<p align="center">
  <h3 align="center">Intermovie</h3>

  <p align="center">
    A study project, house price prediction
  </p>
  
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Anaconda](https://www.anaconda.com/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo

    ```sh
    git clone https://github.com/diem-ai/Immothep.git
    ```

2. Create a conda virtual environment with

    ```sh
    conda create --name <env> --file requirements.txt
    ```

<!-- USAGE EXAMPLES -->
## Usage

* Run the server with:

    ```sh
    uvicorn src.modules.main:app --reload --port 5003
    ```

* Run immothep.ipynb