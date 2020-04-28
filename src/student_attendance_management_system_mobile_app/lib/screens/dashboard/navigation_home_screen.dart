import 'package:sams/theme/app_theme.dart';
import 'package:sams/ui/custom_drawer/drawer_user_controller.dart';
import 'package:sams/screens/dashboard/home_drawer.dart';
import 'package:sams/screens/more/about.dart';
import 'package:sams/screens/more/feedback.dart';
import 'package:sams/screens/dashboard/courses_dashboard.dart';
import 'package:flutter/material.dart';

class NavigationHomeScreen extends StatefulWidget {
  @override
  _NavigationHomeScreenState createState() => _NavigationHomeScreenState();
}

class _NavigationHomeScreenState extends State<NavigationHomeScreen> {
  Widget screenView;
  DrawerIndex drawerIndex;
  AnimationController sliderAnimationController;
  final CoursesDashboard coursesDashboard= CoursesDashboard();
  final AboutScreen aboutScreen= AboutScreen();
  final FeedbackScreen feedbackScreen = FeedbackScreen();

  @override
  void initState() {
    drawerIndex = DrawerIndex.HOME;
    screenView = coursesDashboard;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      color: AppTheme.nearlyWhite,
      child: SafeArea(
        top: false,
        bottom: false,
        child: Scaffold(
          backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
          body: DrawerUserController(
            screenIndex: drawerIndex,
            drawerWidth: MediaQuery.of(context).size.width * 0.75,
            animationController: (AnimationController animationController) {
              sliderAnimationController = animationController;
            },
            onDrawerCall: (DrawerIndex drawerIndexdata) {
              changeIndex(drawerIndexdata);
            },
            screenView: screenView,
          ),
        ),
      ),
    );
  }

  void changeIndex(DrawerIndex drawerIndexdata) {
    if (drawerIndex != drawerIndexdata) {
      drawerIndex = drawerIndexdata;
      if (drawerIndex == DrawerIndex.HOME) {
        setState(() {
          screenView = coursesDashboard;
        });
      } else if (drawerIndex == DrawerIndex.About) {
        setState(() {
          screenView = aboutScreen;
        });
      } else if (drawerIndex == DrawerIndex.FeedBack) {
        setState(() {
          screenView = feedbackScreen;
        });
      }
    }
  }
}
