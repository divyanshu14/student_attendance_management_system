
import 'package:flutter/material.dart';
import 'package:sams/models/user_info.dart';
import 'package:sams/screens/instructor/instructor_course_screen.dart';
import 'package:sams/screens/student_pages/student_course_screen.dart';
import 'package:sams/theme/app_theme.dart';

class CourseCard extends StatelessWidget {
  final Course course;
  final String role;
  CourseCard({@required this.course,@required this.role});
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Padding(
          padding: const EdgeInsets.only(
              top: 32, left: 8, right: 8, bottom: 0),
          child: Container(
            constraints: BoxConstraints(maxHeight: 150),
            width: double.maxFinite,
            height: double.maxFinite,
            decoration: BoxDecoration(
              boxShadow: <BoxShadow>[
                BoxShadow(
                    color: AppTheme.light.withOpacity(0.6),
                    offset: const Offset(1.1, 4.0),
                    blurRadius: 8.0),
              ],
              gradient: LinearGradient(
                colors: [AppTheme.dark,AppTheme.dark.withOpacity(0.5)],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: const BorderRadius.only(
                bottomRight: Radius.circular(8.0),
                bottomLeft: Radius.circular(8.0),
                topLeft: Radius.circular(8.0),
                topRight: Radius.circular(54.0),
              ),
            ),
            child: Padding(
              padding: const EdgeInsets.only(
                  top: 54, left: 16, right: 16, bottom: 0),
              child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                FittedBox(child:Text(
                  course.name,
                  textAlign: TextAlign.center,
                  style: AppTheme.headlineLight,
                  overflow: TextOverflow.ellipsis,
                ),)
              ],
                ),
            ),
          ),
        ),
        Positioned(
          top: 0,
          left: 0,
          child: Container(
            width: 84,
            height: 84,
            decoration: BoxDecoration(
              color: AppTheme.buildLightTheme().scaffoldBackgroundColor.withOpacity(0.2),
              shape: BoxShape.circle,
            ),

          ),
        ),
        Positioned(
          top: 34,
          left: 8,
          child: SizedBox(
            width: 80,
            height: 80,
            child: Text(course.code.toUpperCase(),
            style: AppTheme.titleLight,
            
            ),
          ),
        ),
        Container(
          constraints: BoxConstraints(maxHeight: 150),
          decoration: BoxDecoration(

            color: Colors.transparent,
            borderRadius: const BorderRadius.only(
                bottomRight: Radius.circular(8.0),
                bottomLeft: Radius.circular(8.0),
                topLeft: Radius.circular(8.0),
                topRight: Radius.circular(54.0),
            ),
          ),
          child: InkWell(
            splashColor: Colors.grey.withOpacity(0.2),
            borderRadius: const BorderRadius.only(
                bottomRight: Radius.circular(8.0),
                bottomLeft: Radius.circular(8.0),
                topLeft: Radius.circular(8.0),
                topRight: Radius.circular(54.0),
            ),
            onTap: () {
                  // FocusScope.of(context).requestFocus(FocusNode());
                  switch (role) {
                    case 'student':{
                      Navigator.push(context, MaterialPageRoute(builder: (context)=>StudentCoursePage(course:course)));
                      break;}
                    case 'instructor':{
                      Navigator.push(context, MaterialPageRoute(builder: (context)=>InstructorCoursePage(course: course)));
                      break;
                    }
                    case 'teachingAssisstant':{
                      Navigator.push(context, MaterialPageRoute(builder: (context)=>InstructorCoursePage(course: course)));
                      break;
                    }
                  }
            },
          ),
        ),
      ],
    );
  }
}