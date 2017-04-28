English-Spanish Translator using Sequence-to-Sequence Models
===================

Table of contents
-------

[TOC]

----------
Authors
-------
This repository is being developed as part of the course  Speech and Speaker Recognition ([DT2119](https://www.kth.se/social/course/DT2119/) / [VT171](https://kth.instructure.com/courses/1730))] at [KTH Royal Institute of Technology](http://kth.se), in the Spring 17 P4 round.

| Author               | GitHub                                            |
|:---------------------|:--------------------------------------------------|
| Sergio López | [Serloapl](https://github.com/Serloapl) |
| Mónica Villanueva | [MonicaVillanueva](https://github.com/MonicaVillanueva)     |
| Diego Yus | [DYusL](https://github.com/DYusL)       |


> **Note:**

> - This repo in currently under development.
> - The **final version** of it will be reached at the begining of **June 2017**.


----------


Description
-------------
The idea of the project is using **Recurrent Neural Networks (RNNs)** to learn the mapping between an input sequence directly to an output sequence. The main idea behind it is to consider the entire input sentence as a unit for translation, in comparison to the previous approach, called Phrase-Based Machine Translation (PBMT) that breaks an input sentence into words and phrases to be translated largely independently.
In our case, a sentence in one language (English) would be translated to that same sentence in another language (Spanish). 

Dataset
-------
There are multiple databases that can be used in order to perform the learning phase. One of the recommended ones is the **European Parliament Proceedings Parallel Corpus**, that can be found at: http://www.statmt.org/europarl/

Libraries
-------
The code will be developed employing **Tensor Flow**, an open library for machine learning originally created by Google.

----------

Aditional resources
-------------------

 - [Original paper](https://arxiv.org/pdf/1409.3215.pdf)
 - [Tensorflow tutorial](https://www.tensorflow.org/tutorials/seq2seq)
