import 'dart:developer';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:sams/theme/app_theme.dart';




class ClickPicture extends StatefulWidget {
  @override
  ClickPictureState createState() => ClickPictureState();
}

class ClickPictureState extends State<ClickPicture> {

  List<CameraDescription> cameras;
  CameraDescription currentCamera;
  CameraController _controller;
  Future _initializeControllerFuture;
  Future _getCameras;

  Future<void> getCameras()async {
    this.cameras = await availableCameras();
    return initiateCamera(this.cameras);
  }

  Future<void> initiateController ()async{
    _controller=CameraController(
      this.currentCamera,
      ResolutionPreset.medium
    );
    return _controller.initialize();
  }

  Future<void> initiateCamera( List<CameraDescription> availableCameras)async{
    this.cameras=availableCameras;
    this.currentCamera=this.cameras.first;
    return initiateController();
  }

  @override
  void initState(){
    super.initState();
    _getCameras= getCameras();
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
          body:
            FutureBuilder<void>(
              future: _getCameras,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  // If the Future is complete, display the preview.
                  return cameraScreen(context);
                } else {
                  // Otherwise, display a loading indicator.
                  return Center(child: CircularProgressIndicator());
                }
              },
            ) 

    );
  }
  Widget cameraScreen(context){
    return Column(
        children: <Widget>[
          Expanded(
            child: Align(
            alignment: Alignment.topCenter,
            child: AspectRatio(
              aspectRatio: _controller.value.aspectRatio,
              child: CameraPreview(_controller)),
            ),
          ),
          Align(
            alignment: Alignment.bottomCenter,
            child:    Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: Colors.red,
                    ),
                    child: InkWell(
                      onTap: ()=>Navigator.pop(context),
                      child: Padding(
                        padding: const EdgeInsets.all(20.0),
                        child: Icon(Icons.cancel,color: Colors.white,),
                      )
                    ),
                  ),
                  Container(
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: Colors.cyan.withOpacity(0.5),
                    ),
                    child: InkWell(
                      child: Padding(
                        padding: const EdgeInsets.all(10.0),
                        child: Icon(Icons.camera,color: Colors.white,size: 40,),
                      ),
                      ),
                  ),
                  Container(
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: Colors.green,
                    ),
                    child: InkWell(
                      child: Padding(
                        padding: const EdgeInsets.all(20.0),
                        child: Icon(Icons.done,color: Colors.white,),
                      )
                    ),
                    ),
                ],
              ),
            ),
            SizedBox(height: 10,),
            Align(
              alignment: Alignment.bottomCenter,
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Container(
                      child: InkWell(
                        onLongPress: ()=> _showImage(context),
                        child: Padding(
                          padding: const EdgeInsets.all(10.0),
                          child: Icon(Icons.image,size: 50,),
                        )
                      ),
                    ),
                    Container(
                      child: InkWell(
                        onTap: ()=> _showImage(context),
                        child: Padding(
                          padding: const EdgeInsets.all(10.0),
                          child: Icon(Icons.image,size: 50,),
                        )
                      ),
                    ),Container(
                      child: InkWell(
                        onTap: ()=> _showImage(context),
                        child: Padding(
                          padding: const EdgeInsets.all(10.0),
                          child: Icon(Icons.image,size: 50,),
                        )
                      ),
                    ),Container(
                      child: InkWell(
                        onTap: ()=> _showImage(context),
                        child: Padding(
                          padding: const EdgeInsets.all(10.0),
                          child: Icon(Icons.image,size: 50,),
                        )
                      ),
                    ),
                  ]
                ),
              )  
          )
        ]
        );
  }

  void _showImage(context){
    Dialog imageDialog= Dialog(
      backgroundColor: AppTheme.buildLightTheme().cardColor,
      elevation: 8.0,
      child: Container(
        decoration: BoxDecoration(
          shape: BoxShape.circle,

        ),
        child: 
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Icon(Icons.image,size: 100,color: Colors.cyan,),
            ),
      ),
    );
    showDialog(context: context, builder: (BuildContext context) =>imageDialog);
    }

}