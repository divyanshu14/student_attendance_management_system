import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/authentication/authentication_bloc.dart';
import 'package:sams/blocs/authentication/authentication_state.dart';
import 'package:sams/screens/dashboard/dashboard_home.dart';
import 'package:sams/screens/login/login_screen_presenter.dart';
import 'package:sams/ui/loading_page.dart';
import 'package:sams/screens/login/login_screen.dart';
import 'package:sams/screens/dashboard/navigation_home_screen.dart';

class OnStartup extends StatelessWidget {

  // @override
  // Widget build(BuildContext context) {
  //   return FutureBuilder(
  //     future: tokenStored,
  //     builder: (BuildContext context, AsyncSnapshot snapshot){
  //       if(snapshot.hasData){
  //       log("Token Present "+ snapshot.data.toString());
  //         if(snapshot.data){
  //           return NavigationHomeScreen();
  //         }
  //         else {
  //           return LoginForm();
  //         }
  //       }
  //       else return CircularProgressIndicator();
  //     }
  //     );
  // }

  @override
  Widget build(BuildContext context){
    return BlocBuilder<AuthenticationBloc, AuthenticationState>(
        builder: (context, state) {
          if (state is AuthenticationUninitialized) {
            return LoadingPage();
          }
          if (state is AuthenticationAuthenticated) {
            return NavigationHomeScreen();
          }
          if (state is AuthenticationUnauthenticated) {
            return LoginPage();
          }
          if (state is AuthenticationLoading) {
            return LoadingPage();
          }
        },
      );
  }


}