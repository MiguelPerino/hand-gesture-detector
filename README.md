# 🖐️ Hand Gesture Detector

Detector de gestos em tempo real com a webcam, usando **MediaPipe** e **OpenCV**. O sistema identifica os landmarks da mão e aplica lógica geométrica personalizada para reconhecer gestos específicos.

Meu primeiro projeto de **Computer Vision** — desenvolvido para aprender os fundamentos de visão computacional e processamento de imagem em tempo real.

---

## ✋ Gestos reconhecidos

| Gesto | Descrição |
|---|---|
| ☝️ Contagem de dedos | Detecta quantos dedos estão levantados (0 a 5) |
| ✌️ Paz | Indicador e médio levantados |
| 👍 Joinha | Somente o polegar levantado e apontando para cima |
| 👎 Negativo | Polegar apontando para baixo, demais fechados |
| 🤙 Hang Loose | Polegar e mindinho levantados |

> A lógica de cada gesto foi implementada manualmente com base nas coordenadas dos landmarks — sem uso de classificadores prontos.

---

## 🛠️ Tecnologias

- **Python 3**
- **OpenCV** — captura e exibição dos frames da webcam
- **MediaPipe** — detecção dos 21 landmarks da mão (Hand Landmarker)
- **Flask** — interface web em desenvolvimento (WIP)

---

## 📁 Estrutura do projeto

```
hand-gesture-detector/
├── main.py                  # Execução via janela local (OpenCV)
├── app.py                   # Servidor Flask com streaming MJPEG (WIP)
├── gesture_detector.py      # Wrapper do MediaPipe HandLandmarker
├── gestures/
│   └── hand_gestures.py     # Lógica de classificação dos gestos
├── utils/
│   └── drawing.py           # Desenho dos landmarks e informações na tela
├── templates/
│   └── index.html           # Interface web (WIP)
├── static/
│   └── style.css            # Estilo da interface web (WIP)
└── requirements.txt
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/hand-gesture-detector.git
cd hand-gesture-detector
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Baixe o modelo do MediaPipe

Faça o download do arquivo `hand_landmarker.task` na [página oficial do MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) e coloque na raiz do projeto.

### 4. Execute

**Via janela local (OpenCV):**
```bash
python main.py
```
Pressione `Q` para encerrar.

**Via interface web (em desenvolvimento):**
```bash
python app.py
```
Acesse `http://localhost:5000` no navegador.

---

## ⚙️ Como funciona

1. A webcam captura os frames em tempo real
2. O **MediaPipe HandLandmarker** detecta até 2 mãos e retorna 21 pontos de referência (landmarks) por mão
3. A lógica em `hand_gestures.py` analisa as coordenadas X e Y desses pontos para determinar se cada dedo está levantado ou abaixado
4. Os gestos são identificados com base na combinação dos dedos ativos
5. O resultado é exibido na tela via OpenCV ou, futuramente, via stream MJPEG no navegador

---

## 🚧 Em desenvolvimento

- [ ] Completar a interface web (Flask + HTML/CSS)
- [ ] Streaming de vídeo funcional no navegador
- [ ] Adicionar novos gestos
- [ ] Melhorar a robustez da detecção em diferentes condições de iluminação

---

## 📚 Referências

- [MediaPipe Hand Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [OpenCV Documentation](https://docs.opencv.org/)