import 'dart:developer';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:path_provider/path_provider.dart';
import 'package:sams/theme/app_theme.dart';
import 'package:path/path.dart';
import 'package:photo_view/photo_view.dart';



class ClickPicture extends StatefulWidget {
  @override
  ClickPictureState createState() => ClickPictureState();
}

class ClickPictureState extends State<ClickPicture> {

  List<CameraDescription> cameras;
  CameraDescription currentCamera;
  CameraController _controller;
  String _imagesPath;
  Future _initializeControllerFuture;
  Future _getCamerasFuture;
  Future<Directory> _imagesPathFuture;
  List<String> _imagesClickedPaths;

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

  Future<Directory> getPath()async{
    return await  getTemporaryDirectory();
  }

  @override
  void initState(){
    super.initState();
    _imagesClickedPaths=List();
    _getCamerasFuture= getCameras();
    _imagesPathFuture= getPath();
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
              future: _getCamerasFuture,
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
                      onTap:()=> _saveImage(context),
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
            SizedBox(height: 15,),
            Align(
              alignment: Alignment.bottomCenter,
              child: Container(
                decoration: BoxDecoration(
                    color: AppTheme.buildLightTheme().primaryColor,
                  ),
                child: InkWell(
                  onTap: ()=>_showImage(context),
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Icon(Icons.image,size: 40,color: Colors.white,),
                  ),
                ),
              )  
          )
        ]
        );
  }



  void setPath(Directory directory){
    _imagesPath=directory.path;
  }

  void _saveImage(context) async{
    try {
      // Ensure that the camera is initialized.
      await _initializeControllerFuture;
      await _imagesPathFuture.then(setPath);
      final path = join(
        _imagesPath,
        '${DateTime.now()}.jpg',
      );
      // Attempt to take a picture and log where it's been saved.
      await _controller.takePicture(path);
      _imagesClickedPaths.add(path);
      log(path);
    } catch (e) {
      print(e);
    }
  }

  void _showImage(context){
    Dialog imageDialog= Dialog(
      backgroundColor: AppTheme.buildLightTheme().cardColor,
      elevation: 8.0,
      child: Material(
        child: Container(
          height: 500,

          child: _imagesClickedPaths.length==0
          ? Center(child: new Text('No Images Yet'))
          : new ListView.builder(
            scrollDirection: Axis.horizontal,
            itemCount: _imagesClickedPaths.length,
            itemBuilder: (BuildContext listContext,int index){
              return _imageViewer(listContext,_imagesClickedPaths[index],index);
            }
            ),
        )
      ),
    );
    showDialog(context: context, builder: (BuildContext context) =>imageDialog);
    }

  Widget _imageViewer(BuildContext context,String path, int index){
    return Container(
      // height: MediaQuery.of(context).size.height,
      width: MediaQuery.of(context).size.width,
      child: Stack(
        children:<Widget>[ 
          Padding(
             padding: EdgeInsets.all(10),
              // width: ,
              child: PhotoView(
                tightMode: true,
              maxScale: 3.0,
              minScale: 1.0,
              imageProvider:FileImage(File (_imagesClickedPaths[index])),
              ),
          ),
          Positioned(
            bottom: MediaQuery.of(context).size.height/10,
            child: FloatingActionButton.extended(
              onPressed: () {
                  _imagesClickedPaths.removeAt(index);
                  Navigator.pop(context);
              },
              label: Padding(
                padding: EdgeInsets.only(top:30,bottom: 30),
                child: Text(
                  'Remove',
                  style: AppTheme.buttonText,
                  ),
              ),
              icon: Icon(
                Icons.cancel,
                color: Colors.white,
              ),
              backgroundColor: AppTheme.secondaryColor,
            ),
          ),
          ]
      ),
    );
  }

}