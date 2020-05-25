# Deepspeech Català

An ASR model created with the Mozilla [DeepSpeech](https://github.com/mozilla/DeepSpeech) engine. (Jump to [english](#deepspeech-catalan-asr-model))

Model de reconeixement de la parla creat amb el motor [DeepSpeech](https://github.com/mozilla/DeepSpeech) de Mozilla. Us podeu descarregar l'última versió [aquí](https://github.com/ccoreilly/deepspeech-catala/releases).

Pots provar el model enviant un missatge vocal al bot de Telegram [DeepSpeechCatalà](https://t.me/DeepSpeechCatalaBot)

## Motivació

La motivació principal és la d'aprendre, pel que el model evoluciona constantment a mida que vaig fent proves. També tenia curiositat per saber
qué era possible amb el corpus lliure actual de [CommonVoice](https://voice.mozilla.org/ca/datasets) (la resposta hauria de motivar a tothom a contribuïr-hi encara més).

## Com fer-lo servir

Descarregueu-vos el model i l'scorer i feu servir el motor d'inferència deepspeech per a inferir el text d'un arxiu audio (16Hz mono WAV)

```
$ pip install deepspeech@0.7.1
$ deepspeech --model deepspeech-catala-0.6.0.pbmm --scorer kenlm.scorer --audio file.wav
```

## Comparativa de models

A continuació una comparativa de les diferents versions del model, el corpus emprat i el resultats de l'avaluació.

Les versions anteriors a la 0.4.0 feien servir un alfabet sense vocals accentuades pel que no es consideren representatius.

### Corpus d'avaluació ParlamentParla

Nota: Per la versió 0.6.0 del model vaig combinar el corpus complet (train, dev i test) de CommonVoice amb el de [ParlamentParlaClean](https://collectivat.cat/asr) per després barrejar-lo i dividir-lo en tres sets: train (75%), dev (20%) i test(5%). D'aquesta manera s'ha augmentat el nombre de dades d'entrenament. Com que degut a això el set test conté dades del corpus CommonVoice que podrien haver estat emprades en l'entrenament dels altres models, s'han avaluat tots els models exclusivament amb 1713 frases que cap model ha mai vist (totes del corpus ParlamentParlaClean).

| Model                                                                 | Corpus                          | Dades augmentades? | WER    | CER    | Loss   |
| --------------------------------------------------------------------- | ------------------------------- | ------------------ | ------ | ------ | ------ |
| deepspeech-catala@0.4.0                                               | CommonVoice                     | No                 | 30,16% | 13,79% | 112,96 |
| deepspeech-catala@0.5.0                                               | CommonVoice                     | Sí                 | 29,66% | 13,84% | 108,52 |
| deepspeech-catala@0.6.0                                               | CommonVoice+ParlamentParlaClean | No                 | 13,85% | 5,62%  | 50,49  |
| [stashify@deepspeech_cat](https://github.com/stashify/deepspeech_cat) | CommonVoice?                    | Sí                 | 22,62% | 13,59% | 80,45  |

### Corpus d'avaluació [FestCat](http://festcat.talp.cat/devel.php)

| Model                                                                 | Corpus                          | Dades augmentades? | WER    | CER    | Loss   |
| --------------------------------------------------------------------- | ------------------------------- | ------------------ | ------ | ------ | ------ |
| deepspeech-catala@0.4.0                                               | CommonVoice                     | No                 | 77,60% | 65,62% | 243,25 |
| deepspeech-catala@0.5.0                                               | CommonVoice                     | Sí                 | 78,12% | 65,61% | 235,60 |
| deepspeech-catala@0.6.0                                               | CommonVoice+ParlamentParlaClean | No                 | 76,10% | 65,16% | 240,69 |
| [stashify@deepspeech_cat](https://github.com/stashify/deepspeech_cat) | CommonVoice?                    | Sí                 | 80,58% | 66,82% | 180,81 |

Aquesta avaluació demostra com el models no generalitzen gaire bé.

El corpus FestCat té una variablititat major pel que fa al nombre de paraules per frase, amb el 90% entre 2 i 23 paraules, mentre que en el corpus de CommonVoice la major part de les frases contenen entre 3 i 16 paraules.

Com era d'esperar, avaluant els models només amb les frases del corpus d'avaluació que contenen 4 o més paraules el resultat millora:

| Model                                                                 | Corpus                          | Dades augmentades? | WER    | CER    | Loss   |
| --------------------------------------------------------------------- | ------------------------------- | ------------------ | ------ | ------ | ------ |
| deepspeech-catala@0.4.0                                               | CommonVoice                     | No                 | 58,78% | 46,61% | 193,85 |
| deepspeech-catala@0.5.0                                               | CommonVoice                     | Sí                 | 58,94% | 46,47% | 188,42 |
| deepspeech-catala@0.6.0                                               | CommonVoice+ParlamentParlaClean | No                 | 56,68% | 46,00% | 189,03 |
| [stashify@deepspeech_cat](https://github.com/stashify/deepspeech_cat) | CommonVoice?                    | Sí                 | 61,11% | 48,16% | 144,78 |

## Possibles següents passos

- Ampliar el corpus de dades d'entrenament
- Optimitzar els paràmetres del model
- Avaluar el model amb un corpus més variat (variants dialectals, soroll, context informal)

# Deepspeech Catalan ASR Model

## Motivation

The main motivation of this project is to learn how to creat ASR models using Mozilla's DeepSpeech engine so the model is constantly evolving. Moreover I wanted to see what was possible with the currently released [CommonVoice](https://voice.mozilla.org/ca/datasets) catalan language dataset.

## Usage

Download the model and the scorer and use the deepspeech engine to infer text from an audio file (16Hz mono WAV)

```
$ pip install deepspeech@0.7.1
$ deepspeech --model deepspeech-catala-0.6.0.pbmm --scorer kenlm.scorer --audio file.wav
```

## Model comparison

What follows is a comparison of the different published model versions, the dataset used and the accuracy of each model.

### Test corpus from ParlamentParla dataset

Note: For version 0.6.0 the whole CommonVoice dataset (train, dev and test files) was combined with the clean dataset of ParlamentParla, shuffled and split in train/dev/test files using a 75/20/5 ratio. Due to this fact, a comparison between the models can only be made by using 1713 sentences from the ParlamentParla dataset not seen by any model during training.

| Model                                                                 | Corpus                          | Augmentation | WER    | CER    | Loss   |
| --------------------------------------------------------------------- | ------------------------------- | ------------ | ------ | ------ | ------ |
| deepspeech-catala@0.4.0                                               | CommonVoice                     | No           | 30,16% | 13,79% | 112,96 |
| deepspeech-catala@0.5.0                                               | CommonVoice                     | Sí           | 29,66% | 13,84% | 108,52 |
| deepspeech-catala@0.6.0                                               | CommonVoice+ParlamentParlaClean | No           | 13,85% | 5,62%  | 50,49  |
| [stashify@deepspeech_cat](https://github.com/stashify/deepspeech_cat) | CommonVoice?                    | Sí           | 22,62% | 13,59% | 80,45  |

### Test corpus from the [FestCat](http://festcat.talp.cat/devel.php) dataset

| Model                                                                 | Corpus                          | Augmentation | WER    | CER    | Loss   |
| --------------------------------------------------------------------- | ------------------------------- | ------------ | ------ | ------ | ------ |
| deepspeech-catala@0.4.0                                               | CommonVoice                     | No           | 77,60% | 65,62% | 243,25 |
| deepspeech-catala@0.5.0                                               | CommonVoice                     | Sí           | 78,12% | 65,61% | 235,60 |
| deepspeech-catala@0.6.0                                               | CommonVoice+ParlamentParlaClean | No           | 76,10% | 65,16% | 240,69 |
| [stashify@deepspeech_cat](https://github.com/stashify/deepspeech_cat) | CommonVoice?                    | Sí           | 80,58% | 66,82% | 180,81 |

Validating the models against the FestCat dataset shows that the models do not generalize well. This corpus has a higer variability in the word count of the test sentences, with 90% of the sentences containing an evenly distributed amount of words between 2 and 23, whilst most of the sentences in the CommonVoice corpus contain between 3 and 16 words.

As expected, validating the models against a test set containing only sentences with 4 or more words improves accuracy:

| Model                                                                 | Corpus                          | Augmentation | WER    | CER    | Loss   |
| --------------------------------------------------------------------- | ------------------------------- | ------------ | ------ | ------ | ------ |
| deepspeech-catala@0.4.0                                               | CommonVoice                     | No           | 58,78% | 46,61% | 193,85 |
| deepspeech-catala@0.5.0                                               | CommonVoice                     | Sí           | 58,94% | 46,47% | 188,42 |
| deepspeech-catala@0.6.0                                               | CommonVoice+ParlamentParlaClean | No           | 56,68% | 46,00% | 189,03 |
| [stashify@deepspeech_cat](https://github.com/stashify/deepspeech_cat) | CommonVoice?                    | Sí           | 61,11% | 48,16% | 144,78 |

## Possible next steps

- Expand the training data with other free datasets
- Tune the model parameters to improve performance
- Validate the models with more varied test datasets (dialects, noise)
