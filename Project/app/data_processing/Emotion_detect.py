from deepface import DeepFace

emotion_translation = {
    'angry': 'Enojo',
    'disgust': 'Desagrado',
    'fear': 'Miedo',
    'happy': 'Felicidad',
    'sad': 'Tristeza',
    'surprise': 'Sorpresa',
    'neutral': 'Neutral'
}#Diccionario de emociones

models_FR = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
  "GhostFaceNet",
]


backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'fastmtcnn',
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
  'centerface',
]


async def emotion_analize(frame):
    """
    Función que recibe los datos de una imagen.
    
    :param frame_data: 
    :return: los tres parametros
    """
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'])
        
        #print(f'Resultado del analisis: {analysis}')
        #analysis0 = DeepFace.analyze(frame,actions=['emotion'],detector_backend=backends[0], enforce_detection=False)
        #analysis2 = DeepFace.analyze(frame,actions=['age','gender',"emotion"])
                
        ##print('orden de emm: ', analysis[0]['emotion'])
        emociones = list((analysis[0]['emotion']).values())
        emociones = [float(valor) for valor in emociones]
        #print(f"las emociones son: {emociones}, y su tipo de elemnto es {type(emociones)}" )
        emotion = analysis[0]["dominant_emotion"]
        #emotion0 = analysis0[0]["dominant_emotion"]
        percentage = int(analysis[0]['emotion'][emotion])
        
        #Reemplazo de los datos
        emotion = emotion_translation.get(emotion, emotion)                        
        
        if percentage < 30:
          percentage = 0
          emotion = 'Desconocida'
          emociones =[0,0,0,0,0,0,0]

        return percentage, emotion, emociones

    except Exception as e:
        print('Error modulo deteccion de emociones')
        percentage = 0
        emotion = 'Desconocida'
        emociones =[0,0,0,0,0,0,0]
        return percentage, emotion, emociones