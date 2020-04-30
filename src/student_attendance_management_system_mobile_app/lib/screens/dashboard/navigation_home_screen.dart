import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/user_data/user_data_bloc.dart';
import 'package:sams/blocs/user_data/user_data_event.dart';
import 'package:sams/theme/app_theme.dart';
import 'package:sams/ui/custom_drawer/drawer_user_controller.dart';
import 'package:sams/screens/dashboard/home_drawer.dart';
import 'package:sams/screens/more/about.dart';
import 'package:sams/screens/more/feedback.dart';
import 'package:sams/screens/dashboard/dashboard_home.dart';
import 'package:flutter/material.dart';

class NavigationHomeScreen extends StatefulWidget {
  @override
  _NavigationHomeScreenState createState() => _NavigationHomeScreenState();
}

class _NavigationHomeScreenState extends State<NavigationHomeScreen> {
  Widget screenView;
  DrawerIndex drawerIndex;
  AnimationController sliderAnimationController;
  final DashboardHome dashboardHome= DashboardHome();
  final AboutScreen aboutScreen= AboutScreen();
  final FeedbackScreen feedbackScreen = FeedbackScreen();

  @override
  void initState() {
    drawerIndex = DrawerIndex.HOME;
    screenView = dashboardHome;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
      body: BlocProvider<UserDataBloc>(
        create: (context) {
          return UserDataBloc()..add(UserDataInitiate());
        },
        child: DrawerUserController(
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
    );
  }

  void changeIndex(DrawerIndex drawerIndexdata) {
    if (drawerIndex != drawerIndexdata) {
      drawerIndex = drawerIndexdata;
      if (drawerIndex == DrawerIndex.HOME) {
        setState(() {
          screenView = dashboardHome;
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
