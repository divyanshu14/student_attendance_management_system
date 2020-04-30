import 'package:flutter/material.dart';

import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/authentication/authentication_bloc.dart';
import 'package:sams/blocs/login/login_bloc.dart';
import 'package:sams/screens/login/forget_password.dart';
import 'package:sams/screens/login/login_form.dart';
import 'package:sams/theme/app_theme.dart';


class LoginPage extends StatelessWidget {

  LoginPage({Key key}): super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: null,
      body: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Padding(
                padding: EdgeInsets.only(top :100.0,right: 40,left:40,bottom:100),
                child: Image.asset('assets/logo.png'),
                ),
            BlocProvider<LoginBloc>(
              create: (context) {
                return LoginBloc(
                  authenticationBloc: BlocProvider.of<AuthenticationBloc>(context),
                );
              },
              child: LoginForm(),
            ),
            _getForgetButton(context),
          ],
        ),
      ),
    );
  }

  Widget _getForgetButton(BuildContext context){
    return Padding(
      padding: EdgeInsets.all(20),
      child: Container(
        decoration: BoxDecoration(
          color: Colors.transparent,

        ),
        child: InkWell(
          highlightColor: AppTheme.buildLightTheme().highlightColor,
          splashColor: AppTheme.buildLightTheme().splashColor,
          child: Text(
            'Forgot Password ?',
            style: AppTheme.body1
          ),
          onTap: (){
              FocusScope.of(context).requestFocus(FocusNode());
              Navigator.push(context, MaterialPageRoute(builder: (context)=>ForgetPassword()));
          },
        ),
      ),
    );
  }
}
