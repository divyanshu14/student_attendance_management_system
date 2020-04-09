import 'dart:developer';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';




class ClickPicture extends StatefulWidget {
  @override
  ClickPictureState createState() => ClickPictureState();
}

class ClickPictureState extends State<ClickPicture> {

  List<CameraDescription> cameras;
  CameraDescription currentCamera;
  CameraController _controller;
  Future _initializeControllerFuture;

  Future<List<CameraDescription>> getCameras()async {
    this.cameras = await availableCameras();
    return this.cameras;
  }

  void intiateController (){
    _controller=CameraController(
      this.currentCamera,
      ResolutionPreset.medium
    );
    _initializeControllerFuture = _controller.initialize();

  }

  void intiateCamera( List<CameraDescription> availableCameras){
    this.cameras=availableCameras;
    this.currentCamera=this.cameras.first;
    intiateController();
  }

  @override
  void initState(){
    super.initState();
    getCameras().then(intiateCamera);
    
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    intiateController();

    return Scaffold(
          body:

            FutureBuilder<void>(
              future: _initializeControllerFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  // If the Future is complete, display the preview.
                  return cameraScreen();
                } else {
                  // Otherwise, display a loading indicator.
                  return Center(child: CircularProgressIndicator());
                }
              },
            ) 

    );
  }
  Widget cameraScreen(){
    return Stack(
        children: <Widget>[
          Align(
            alignment: Alignment.topCenter,
          child: AspectRatio(
            aspectRatio: _controller.value.aspectRatio,
            child: CameraPreview(_controller)),
          ),
          Align(
            alignment: Alignment.bottomCenter,
            child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,

              children: <Widget>[
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Container(
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: Colors.cyan.withOpacity(0.5),
                      ),
                      child: InkWell(
                        child: Padding(
                          padding: const EdgeInsets.all(40.0),
                          child: Icon(Icons.camera,color: Colors.white,),
                        ),
                        ),
                    ),
                  ],
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Container(
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: Colors.cyan.withOpacity(0.5),
                      ),
                      child: InkWell(
                        child: Padding(
                          padding: const EdgeInsets.all(40.0),
                          child: Icon(Icons.camera,color: Colors.white,),
                        ),
                        ),
                    ),
                  ],                    
                )
              ],
            )
          )
        ]
        );

  }

}