
<p  align="center">
<h1  align="center">Immothep</h3>
</p>

## Table of Contents

*  [About the Project](#about-the-project)

*  [Built With](#built-with)

*  [Getting Started](#getting-started)

*  [Installation](#installation)

*  [Usage](#usage)

*  [Authors](#authors)

## About The Project

Immothep, the new flagship of French real estate, wants to create a property valuation module based on artificial intelligence to enrich its platform and acquire new buyers / sellers.

## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
```git
git clone https://github.com/diem-ai/Immothep.git
```
2. Create a conda virtual environment with
```bash
conda create --name <env> --file package-list.txt
```
## Usage


- Run [notebook_main.ipynb](https://github.com/KRDavid/Immothep/blob/main/NoteBookBordeaux.ipynb)
> This will generate essential files for server execution such as [modele_lineaire_maison.p](https://github.com/Nicolas-Malgat/Immothep/blob/master/modele_lineaire_maison.p), [modele_lineaire_appartement.p](https://github.com/Nicolas-Malgat/Immothep/blob/master/modele_lineaire_appartement.p), **maison_filtre.csv** and **appartement_filtre.csv**.

- Run the server with:
```bash
server.bat
```
or
```bash
uvicorn src.modules.main:app --port 5003
```
- Use the following URL to get an estimation such as:

http://127.0.0.1:5003/estimate?metre_carre=30&nb_pieces=4&terrain=0&code_postal=1000
```JSON
{
	"request":
		{
			"metre_carre":30.0,
			"nb_pieces":4,
			"terrain":0.0,
			"code_postal":1000
		},
	"response":
		{
			"estimation_maison":99560.0362345221,
			"estimation_appart":63630.20351964372
		}
}
```
> This application can't estimate on every "code_postal" unfortunatly.
> A second url can be called in order to get every possible code_postal
> http://127.0.0.1:5003/code_postal

## Authors

Nicolas Campion
Nicolas Malgat