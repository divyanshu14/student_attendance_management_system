import 'dart:io';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/authentication/authentication_bloc.dart';
import 'package:sams/blocs/authentication/authentication_event.dart';
import 'package:sams/onStartup.dart';
import 'package:sams/routes.dart';
import 'package:sams/theme/app_theme.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:sams/utils/constants.dart';


void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setPreferredOrientations(<DeviceOrientation>[DeviceOrientation.portraitUp, DeviceOrientation.portraitDown])
      .then((_) => runApp(MyApp()));
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.dark,
      statusBarBrightness: Platform.isAndroid ? Brightness.light : Brightness.light,
      systemNavigationBarColor: Colors.transparent,
      systemNavigationBarDividerColor: Colors.transparent,
      systemNavigationBarIconBrightness: Brightness.dark,
    ));
    return BlocProvider<AuthenticationBloc>(
      create: (context){
        return AuthenticationBloc()..add(AppStarted());
      },
      child:  MaterialApp(
        title: Constants.APP_TITLE,
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primarySwatch: Colors.cyan,
          textTheme: AppTheme.textTheme,
        ),
        // onGenerateRoute: Router().generateRoute,
        home: OnStartup(),
      )
    );
  }
}
