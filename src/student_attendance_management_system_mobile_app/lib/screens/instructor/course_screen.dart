import 'package:sams/theme/app_theme.dart';
import 'package:flutter/material.dart';
import 'package:sams/models/course.dart';
import 'package:sams/ui/course_card.dart';

class InstructorCoursePage extends StatefulWidget {
  final Course course;
  InstructorCoursePage(this.course);
  @override
  _InstructorCoursePageState createState() => _InstructorCoursePageState();
}

class _InstructorCoursePageState extends State<InstructorCoursePage> with TickerProviderStateMixin {
  List<Course> courseList ;
  AnimationController animationController;
  bool multiple = true;

  @override
  void initState() {
    courseList=[
      Course(name: widget.course.name,code: widget.course.code,),
    ];
    animationController = AnimationController(
        duration: const Duration(milliseconds: 1000), vsync: this);
    super.initState();
  }

  Future<bool> getData() async {
    await Future<dynamic>.delayed(const Duration(milliseconds: 0));
    return true;
  }

  @override
  void dispose() {
    animationController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: _appBar(context),
      floatingActionButton: _takeAttendanceButton(context),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
      body:
       FutureBuilder<bool>(
        future: getData(),
        builder: (BuildContext context, AsyncSnapshot<bool> snapshot) {
          if (!snapshot.hasData) {
            return const SizedBox();
          } 
          else {
            return Padding(
              padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top),
              child: ListView(
                // mainAxisAlignment: MainAxisAlignment.start,
                children: <Widget>[
                  _courseInfoCard(),
                  _lastAttendance(),
                  Row(
                  children: <Widget>[
                    _eventItem('Lecture'),
                    _eventItem('Tutorial'),
                    _eventItem('Labs')
                  ],)
                  

                ]
              ),
            );
          }    
        }
      ),
    );
  }

    
  Widget _appBar(context){
    return AppBar(
      leading: SizedBox(
        width: AppBar().preferredSize.height,
        height: AppBar().preferredSize.height,
        child: InkWell(
          borderRadius:
              BorderRadius.circular(AppBar().preferredSize.height),
          child: Icon(
            Icons.arrow_back_ios,
            color: AppTheme.buildLightTheme().iconTheme.color,
          ),
          onTap: () {
            Navigator.pop(context);
          },
        ),
      ),
      title: Text(widget.course.code,
        style: AppTheme.headline,
      ),
      centerTitle: true,
      backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
      elevation: 0.0,
    );
  }


  Widget _takeAttendanceButton(context){
    return FloatingActionButton.extended(
      onPressed: () {
        // Add your onPressed code here!
      },
      label: Padding(
        padding: EdgeInsets.only(top:30,bottom: 30),
        child: Text(
          'Take Attendance',
          style: AppTheme.buttonText,
          ),
      ),
      icon: Icon(
        Icons.camera_alt,
        color: Colors.white,
      ),
      backgroundColor: AppTheme.secondaryColor,
    );
  }

  Widget _courseInfoCard(){
    return Padding(
      padding: EdgeInsets.only(left: 10,right: 10, top: 20,bottom: 10),
      child: Container(
        decoration: BoxDecoration(
          // color: AppTheme.buildLightTheme().cardColor,
          // borderRadius: BorderRadius.only(
          //     topLeft: Radius.circular(58.0),
          //     bottomLeft: Radius.circular(8.0),
          //     bottomRight: Radius.circular(8.0),
          //     topRight: Radius.circular(58.0)),
          // boxShadow: <BoxShadow>[
          //   BoxShadow(
          //       color: AppTheme.grey.withOpacity(0.2),
          //       offset: Offset(1.1, 1.1),
          //       blurRadius: 10.0),
          // ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Expanded(
                    child: Padding(
                    padding: EdgeInsets.all(20),
                    child: Text(
                      widget.course.name,
                      style: AppTheme.title,
                      overflow: TextOverflow.ellipsis,
                      textAlign: TextAlign.center,
                      maxLines: 2,
                    ),
                  ),
                )
            ],),
            // Padding(padding: EdgeInsets.only(left:20, right: 20) ,child: Divider()),
            Row(
              children: <Widget>[
                Padding(
                padding: EdgeInsets.all(20),
                child: Text(
                  'Total students: '+ (widget.course.studentList?.length ?? '0') ,
                  style: AppTheme.body1,
                ),
                  ),
              ],
            ),
            // Divider(),
            // some other course info
          ],
          
          ),

      ),
    );

  }

  Widget _lastAttendance(){
    return Padding(
      padding: EdgeInsets.all(10),
      child: Container(
        decoration: BoxDecoration(
          color: AppTheme.white,
          borderRadius: BorderRadius.only(
              topLeft: Radius.circular(8.0),
              bottomLeft: Radius.circular(8.0),
              bottomRight: Radius.circular(68.0),
              topRight: Radius.circular(68.0)),
          boxShadow: <BoxShadow>[
            BoxShadow(
                color: AppTheme.grey.withOpacity(0.2),
                offset: Offset(1.1, 1.1),
                blurRadius: 10.0),
          ],
        ),
        child: Column(
          children: <Widget>[
            Padding(
              padding:
                  const EdgeInsets.only(top: 16, left: 16, right: 24),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Padding(
                    padding: const EdgeInsets.only(
                        left: 4, bottom: 0, top: 0),
                    child: Text(
                      'Last Attendance',
                      textAlign: TextAlign.center,
                      style: AppTheme.body1),
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: <Widget>[
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: <Widget>[
                          Padding(
                            padding: const EdgeInsets.only(
                                left: 4, bottom: 8),
                            child: Text(
                              '90',
                              textAlign: TextAlign.center,
                              style: AppTheme.title
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.only(
                                left: 8, bottom: 8),
                            child: Text(
                              '%',
                              textAlign: TextAlign.center,
                              style: AppTheme.title
                            ),
                          ),
                        ],
                      ),
                      Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: <Widget>[
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: <Widget>[
                              Icon(
                                Icons.access_time,
                                color: AppTheme.grey
                                    .withOpacity(0.5),
                                size: 16,
                              ),
                              Padding(
                                padding:
                                    const EdgeInsets.only(left: 4.0),
                                child: Text(
                                  'Today 8:26 AM',
                                  textAlign: TextAlign.center,
                                  style: TextStyle(
                                    fontFamily:
                                        AppTheme.fontName,
                                    fontWeight: FontWeight.w500,
                                    fontSize: 14,
                                    letterSpacing: 0.0,
                                    color: AppTheme.grey
                                        .withOpacity(0.5),
                                  ),
                                ),
                              ),
                            ],
                          ),
                          Padding(
                            padding: const EdgeInsets.only(
                                top: 4, bottom: 14),
                            child: Text(
                              'Lecture',
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontFamily: AppTheme.fontName,
                                fontWeight: FontWeight.w500,
                                fontSize: 12,
                                letterSpacing: 0.0,
                                color: AppTheme.dark,
                              ),
                            ),
                          ),
                        ],
                      )
                    ],
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
                  
  }

  Widget _eventItem(String event){
    return 
    Expanded(
        child: Padding(
    padding: EdgeInsets.only(left:5,right:5, top:16, bottom: 0),
    child: Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
                        colors: [AppTheme.light,AppTheme.dark],
                        begin: Alignment.topLeft,
                        end: Alignment.bottomRight,
                      ),
        borderRadius: BorderRadius.only(
            topLeft: Radius.circular(8.0),
            bottomLeft: Radius.circular(8.0),
            bottomRight: Radius.circular(8.0),
            topRight: Radius.circular(48.0)),
        boxShadow: <BoxShadow>[
          BoxShadow(
              color: AppTheme.grey.withOpacity(0.2),
              offset: Offset(1.1, 1.1),
              blurRadius: 10.0),
        ],
      ),
      child:  Padding(
          padding: const EdgeInsets.only(
              top: 20, left: 16, right: 16, bottom: 10),
          child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text(
              event,
              textAlign: TextAlign.center,
              style: AppTheme.titleLight,
              overflow: TextOverflow.ellipsis,
              ),
            Divider(),
            Text(
              'Total Number',
              style: AppTheme.body2,
              maxLines: 2,
            ),
            SizedBox(height: 8,),
            Center(
              child: Text(
                '10',
                style: AppTheme.titleLight,
                textAlign: TextAlign.center,
              ),
            ),
            Divider(),
            Text(
              'Average Attendance',
              style: AppTheme.body2,
              maxLines: 2,
            ),
            SizedBox(height: 8,),
            Center(
              child: Text(
                '100%',
                style: AppTheme.titleLight,
                  textAlign: TextAlign.center,
              ),
            ),

          ],
            ),
        ),
    ),
        ),
      );
  }

}


