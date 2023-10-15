import torch
 
def yolov5_model():
    # GPU
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # Model
    model = torch.hub.load('./yolov5-5.0',   
                          'best',
                           pretrained=True,
                           source='local')  # or yolov5m, yolov5l, yolov5x, custom
    model = model.to(device)
    return model
 
model = yolov5_model()
