import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:sams/screens/login/login_screen.dart';
import 'package:sams/screens/dashboard/navigation_home_screen.dart';
import 'package:sams/utils/user_token.dart';

class OnStartup extends StatefulWidget {

  @override
  _OnStartupState createState() => _OnStartupState();
}

class _OnStartupState extends State<OnStartup> {
  Future<bool> tokenStored;

  @override
  void initState() {
    tokenStored=UserToken.fetchToken();  
    super.initState();
  }
  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: tokenStored,
      builder: (BuildContext context, AsyncSnapshot snapshot){
        if(snapshot.hasData){
        log("Token Present "+ snapshot.data.toString());
          if(snapshot.data){
            return NavigationHomeScreen();
          }
          else {
            return LoginScreen();
          }
        }
        else return CircularProgressIndicator();
      }
      );
  }
}