import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/course/course_info_bloc.dart';
import 'package:sams/blocs/course/course_info_event.dart';
import 'package:sams/blocs/course/course_info_state.dart';
import 'package:sams/screens/instructor/daily_attendance.dart';
import 'package:sams/screens/take_attendance/click_picture.dart';
import 'package:sams/theme/app_theme.dart';
import 'package:flutter/material.dart';
import 'package:sams/models/user_info.dart';
import 'package:sams/models/course_info.dart';

class InstructorCoursePage extends StatefulWidget {
  final Course course;
  InstructorCoursePage({@required this.course});
  @override
  _InstructorCoursePageState createState() => _InstructorCoursePageState();
}

class _InstructorCoursePageState extends State<InstructorCoursePage> with TickerProviderStateMixin {
  AnimationController animationController;
  bool multiple = true;

  @override
  void initState() {

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
    return  BlocProvider<CourseInfoBloc>(
      create: (context) {
        return CourseInfoBloc(courseCode: widget.course.code)..add(CourseInfoInitiate());
      },
      child:Scaffold(
        appBar: _appBar(context),
        floatingActionButton: _takeAttendanceButton(context),
        floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
        backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
        body: Padding(
          padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top),
          child: ListView(
            children: <Widget>[
              _courseInfoCard(),
              _lastAttendance(),
              Row(
              children: <Widget>[
                _eventItem('Lectures'),
                _eventItem('Tutorials'),
                _eventItem('Practicals')
              ],),
              ViewMembers('Students'),
              ViewMembers('Instructors'),
              ViewMembers('TAs'),
              //sized box to prevent TA card from hiding under FAB
              SizedBox(height: 75,)
            ]
          ),
        ),
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
        Navigator.push(context, MaterialPageRoute(builder: (context)=>ClickPicture()));
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
          color: AppTheme.buildLightTheme().cardColor,
          borderRadius: BorderRadius.only(
              topLeft: Radius.circular(48.0),
              bottomLeft: Radius.circular(48.0),
              bottomRight: Radius.circular(48.0),
              topRight: Radius.circular(48.0)),
          boxShadow: <BoxShadow>[
            BoxShadow(
                color: AppTheme.grey.withOpacity(0.2),
                offset: Offset(1.1, 1.1),
                blurRadius: 10.0),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Expanded(
                    child: Padding(
                    padding: EdgeInsets.all(8),
                    child: Text(
                      widget.course.name,
                      style: AppTheme.title,
                      overflow: TextOverflow.ellipsis,
                      textAlign: TextAlign.center,
                      maxLines: 2,
                    ),
                  ),
                )
            ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                BlocBuilder<CourseInfoBloc, CourseInfoState>(
                    builder: (context, state) {
                      if( state is CourseInfoSuccess){
                        return Text(state.courseInfo.acadYearStart.toString()+'-'+state.courseInfo.acadYearEnd.toString());
                      }
                      if (state is CourseInfoFailure){
                        return Text('');
                      }
                      else return Text('Loading...');
                    }
                  ),
              ],),
            Row(
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.all(20),
                  child: Text('Total students:',
                  style: AppTheme.body1,
                  ),
                ),
                Padding(
                  padding: EdgeInsets.all(8),
                  child: BlocBuilder<CourseInfoBloc, CourseInfoState>(
                    builder: (context, state) {
                      if( state is CourseInfoSuccess){
                        return Text(state.courseInfo.registeredStudents.length.toString());
                      }
                      if (state is CourseInfoFailure){
                        return Text('');
                      }
                      else return Text('Loading...');
                    }
                  ),
                ),
              ],
            ),
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
          borderRadius: BorderRadius.circular(48),
          boxShadow: <BoxShadow>[
            BoxShadow(
                color: AppTheme.grey.withOpacity(0.2),
                offset: Offset(1.1, 1.1),
                blurRadius: 10.0),
          ],
        ),
        child: InkWell(
          onTap: ()=> Navigator.push(context, MaterialPageRoute(builder: (context)=>DailyAttendance())),
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
              child: BlocBuilder<CourseInfoBloc, CourseInfoState>(
                builder: (context, state) {
                  if( state is CourseInfoSuccess){
                    int totalNumber=0;
                    switch (event) {
                      case 'Lectures': {
                        totalNumber=state.courseInfo.totalLecturesHeld;
                        break;
                      }
                      case 'Tutorials': {
                        totalNumber=state.courseInfo.totalTutorialsHeld;
                        break;
                      }
                      case 'Practicals': {
                        totalNumber=state.courseInfo.totalPracticalsHeld;
                        break;
                      }    
                      default:
                    }
                    return Text(
                      totalNumber.toString(),
                      style: AppTheme.titleLight,
                      maxLines: 1,
                    );
                  }
                  if (state is CourseInfoFailure){
                    return Text('');
                  }
                  else return Text('Loading...');
                }
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


class ViewMembers extends StatelessWidget{

  final String memberType;

  ViewMembers(this.memberType);

  @override
  Widget build(BuildContext context){
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Material(
          color: AppTheme.white,
          borderRadius: BorderRadius.circular(48),
          child: InkWell(
            borderRadius: BorderRadius.circular(48),
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Center(
                child: Text(
                  'View '+memberType,
                  style: AppTheme.title,
                  overflow: TextOverflow.ellipsis,
                  textAlign: TextAlign.center,
                  maxLines: 2,
                ),
              ),
            ),
            onTap: (){
              showBottomSheet(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(48)
                ),
                context: context,
                builder: (context) => Container(
                  constraints: BoxConstraints(
                    maxHeight: MediaQuery.of(context).size.height/2
                  ),
                  decoration: BoxDecoration(
                    color: AppTheme.white,
                    borderRadius: BorderRadius.only(topLeft: Radius.circular(48), topRight: Radius.circular(48)),
                  ),            
                  child: 
                  BlocBuilder<CourseInfoBloc, CourseInfoState>(
                    builder: (context, state) {
                      if( state is CourseInfoSuccess){
                        switch (memberType) {
                          case 'Students':{
                            return studentsListViewer(state);
                            }
                          case 'Instructors': return instructorsListViewer(state);
                          case 'TAs': return tAListViewer(state);
                        }
                      }
                      else 
                      return Container(child: CircularProgressIndicator());
                    }
                  )
                ),
              );
            },
          ) 
        ),
    );
  }
  Widget studentsListViewer(CourseInfoSuccess state){
    return Padding(
      padding: const EdgeInsets.only(top :38.0),
      child: ListView.separated(
        itemCount: state.courseInfo.registeredStudents.length,
        itemBuilder: (BuildContext context, int index){
          return Padding(
            padding: EdgeInsets.all(20),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                Text(
                  state.courseInfo.registeredStudents[index].user.firstName,
                  style: AppTheme.title,
                ),
                Spacer(),
                Text(
                  state.courseInfo.registeredStudents[index].entryNumber,
                  style: AppTheme.body1,
                )
              ],
            ),
            );
        },
        separatorBuilder: (context,index){
          return Divider();
        },

      ),
    );
  }

  Widget instructorsListViewer(CourseInfoSuccess state){
    return Padding(
      padding: const EdgeInsets.only(top :38.0),
      child: ListView.separated(
        itemCount: state.courseInfo.instructors.length,
        itemBuilder: (BuildContext context, int index){
          return Padding(
            padding: EdgeInsets.all(20),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                Text(
                  state.courseInfo.instructors[index].classEventCoordinator.user.firstName,
                  style: AppTheme.title,
                ),
                Spacer(),
                Text(
                  state.courseInfo.instructors[index].instructorId,
                  style: AppTheme.body1,
                )
              ],
            ),
            );
        },
        separatorBuilder: (context,index){
          return Divider();
        },

      ),
    );
  }

  Widget tAListViewer(CourseInfoSuccess state){
    return Padding(
      padding: const EdgeInsets.only(top :38.0),
      child: ListView.separated(
        itemCount: state.courseInfo.teachingAssistants.length,
        itemBuilder: (BuildContext context, int index){
          return Padding(
            padding: EdgeInsets.all(20),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                Text(
                  state.courseInfo.teachingAssistants[index].classEventCoordinator.user.firstName,
                  style: AppTheme.title,
                ),
                Spacer(),
                Text(
                  state.courseInfo.teachingAssistants[index].teachingAssistantId,
                  style: AppTheme.body1,
                )
              ],
            ),
            );
        },
        separatorBuilder: (context,index){
          return Divider();
        },

      ),
    );
  }

}