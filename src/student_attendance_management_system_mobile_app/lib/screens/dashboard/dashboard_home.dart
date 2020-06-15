import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/user_data/user_data_bloc.dart';
import 'package:sams/blocs/user_data/user_data_state.dart';
import 'package:sams/models/user_info.dart';
import 'package:sams/theme/app_theme.dart';
import 'package:flutter/material.dart';
import 'package:sams/ui/course_card.dart';

class DashboardHome extends StatefulWidget {
  @override
  _DashboardHomeState createState() => _DashboardHomeState();
}

class _DashboardHomeState extends State<DashboardHome> with TickerProviderStateMixin {

  AnimationController animationController;
  Future<User> user;
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
    return Scaffold(
      backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
      body: Padding(
        padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top),
        child: BlocBuilder<UserDataBloc,UserDataState>(
        builder:(BuildContext context, UserDataState state) {
            if (state is UserDataSuccess){
              return Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  appBar(),
                  courseListPresenter(state.userInfo.studentForCourses,'student'),
                  courseListPresenter(state.userInfo.instructorForCourses,'instructor'),
                  courseListPresenter(state.userInfo.teachingAssistantForCourses,'teachingAssitant')
                ],
              );
            } 
            else {
              return Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children: <Widget>[
                  appBar(),
                  Center(child: CircularProgressIndicator(),)
                ],
              );
            }
          }
        )
      ),
    );
  }

  Widget appBar() {
    return SizedBox(
      height: AppBar().preferredSize.height,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.only(top: 8, left: 8),
            child: Container(
              width: AppBar().preferredSize.height - 8,
              height: AppBar().preferredSize.height - 8,
            ),
          ),
          Expanded(
            child: Center(
              child: Padding(
                padding: const EdgeInsets.only(top: 4),
                child: Text(
                  'Your Courses',
                  style: AppTheme.headline,
                ),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 8, right: 8),
            child: Container(
              width: AppBar().preferredSize.height - 8,
              height: AppBar().preferredSize.height - 8,
              color: Colors.transparent,
              child: Material(
                color: Colors.transparent,
                child: InkWell(
                  borderRadius:
                      BorderRadius.circular(AppBar().preferredSize.height),
                  child: Icon(
                    multiple ? Icons.dashboard : Icons.view_agenda,
                    color: AppTheme.buildLightTheme().iconTheme.color,
                  ),
                  onTap: () {
                    setState(() {
                      multiple = !multiple;
                    });
                  },
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget courseListPresenter(List<Course> courseList, String role){
          if (courseList ==null||courseList.length==0){
            return Divider();
          }
          return Expanded(
            child: GridView(
              padding: const EdgeInsets.only(
                  top: 0, left: 12, right: 12),
              physics: const BouncingScrollPhysics(),
              scrollDirection: Axis.vertical,
              children: List<Widget>.generate(
                courseList.length,
                (int index) {
                  final int count = courseList.length;
                  final Animation<double> animation =
                      Tween<double>(begin: 0.0, end: 1.0).animate(
                    CurvedAnimation(
                      parent: animationController,
                      curve: Interval((1 / count) * index, 1.0,
                          curve: Curves.fastOutSlowIn),
                    ),
                  );
                  animationController.forward();
                  return CourseListView(
                    animation: animation,
                    animationController: animationController,
                    course: courseList[index],
                    role: role,
                  );
                },
              ),
              gridDelegate:
                  SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: multiple ? 2 : 1,
                mainAxisSpacing: 12.0,
                crossAxisSpacing: 12.0,
                childAspectRatio: 1.5,
              ),
            ),
          );            
  }

}

class CourseListView extends StatelessWidget {
  const CourseListView(
      {Key key,
      this.role,
      this.course,
      this.callBack,
      this.animationController,
      this.animation})
      : super(key: key);

  final Course course;
  final VoidCallback callBack;
  final AnimationController animationController;
  final Animation<dynamic> animation;
  final String role;

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: animationController,
      builder: (BuildContext context, Widget child) {
        return FadeTransition(
          opacity: animation,
          child: Transform(
            transform: Matrix4.translationValues(
                0.0, 50 * (1.0 - animation.value), 0.0),
            child: CourseCard(
              course: course,
              role: role,
            ),
          ),
        );
      },
    );
  }
}
