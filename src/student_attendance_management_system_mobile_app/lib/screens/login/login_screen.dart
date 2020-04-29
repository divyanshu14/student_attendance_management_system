import 'dart:developer';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/login/login_bloc.dart';
import 'package:sams/blocs/login/login_events.dart';
import 'package:sams/blocs/login/login_state.dart';
import 'package:sams/screens/login/forget_password.dart';
import 'package:sams/theme/app_theme.dart';
import 'package:sams/utils/constants.dart';

import 'login_screen_presenter.dart';

class LoginForm extends StatefulWidget {
  @override
  _LoginFormState createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {

  final _formKey = new GlobalKey<FormState>();
  String _email,_password;


  // _LoginScreenState() {
  //   _presenter = new LoginScreenPresenter(this);
  // }

  // void _submit() {
  //   final form = _formKey.currentState;
  //   log('sending credentials');
  //   if (form.validate()) {
  //     setState(() => _isLoading = true);
  //     form.save();
  //     // _presenter.doLogin(_username, _password);
  //   }
  // }


  // @override
  // void onLoginError(String errorTxt) {
  //   _showSnackBar("Unable To Login");
  //   setState(() => _isLoading = false);
  // }

  // @override
  // void onLoginSuccess() async {
  //   _showSnackBar('Successful');
  //   setState(() => _isLoading = false);
  //   Navigator.pushNamedAndRemoveUntil(context, Constants.DASHBOARD_ROUTE, ModalRoute.withName(Constants.STARTUP_ROUTE));
  // }

  void _showSnackBar(String text) {
    Scaffold.of(context)
        .showSnackBar(new SnackBar(content: new Text(text), duration: Duration(seconds: 1), backgroundColor: AppTheme.buildLightTheme().primaryColor,));
  }

  void _onLoginButtonPressed() {
    _formKey.currentState.save();
      BlocProvider.of<LoginBloc>(context).add(
        LoginButtonPressed(
          email: _email,
          password: _password,
        ),
      );
    }


@override
  Widget build(BuildContext context) {
    return BlocListener<LoginBloc, LoginState>(
      listener: (context, state) {
        if (state is LoginFailure) {
          _showSnackBar(state.error);
        }
      },
      child: BlocBuilder<LoginBloc, LoginState>(
        builder: (context, state) {
          return Form(
            key: _formKey,
            child: Column(
              children: [
                _getUserIdField(context),
                _getPasswordField(context),
                _getLoginButton(context),  
                Container(
                  child: state is LoginLoading
                      ? CircularProgressIndicator()
                      : null,
                ),
              ],
            ),
          );
        },
      ),
    );
  }

  // @override
  // Widget build(BuildContext context) {
  //   return Scaffold(
  //     key: scaffoldKey,
  //     body: Container(
  //       width: double.infinity,
  //       child: Form(
  //         key: _formKey,
  //         child: SingleChildScrollView(
  //           child: Column(
  //             mainAxisAlignment: MainAxisAlignment.center,
  //             crossAxisAlignment: CrossAxisAlignment.center,
  //             children: <Widget>[
  //               Padding(
  //                 padding: EdgeInsets.only(top :100.0,right: 40,left:40,bottom:100),
  //                 child: Image.asset('assets/logo.png'),
  //                 ),
  //               
  //               _getForgetButton(context),
  //               ],
  //           ),
  //         ),
  //       ),
  //     )
  //   );
  // }

  Widget _getPasswordField(BuildContext context){
    return Padding(
      padding: const EdgeInsets.only(
              left: 16, right: 16, top: 4, bottom: 4),
      child:Container(
        decoration: BoxDecoration(
          color: AppTheme.buildLightTheme().backgroundColor,
          borderRadius: const BorderRadius.all(
            Radius.circular(38.0),
          ),
          boxShadow: <BoxShadow>[
            BoxShadow(
                color: Colors.grey.withOpacity(0.2),
                offset: const Offset(0, 2),
                blurRadius: 8.0),
          ],
        ),
        child: Padding(
          padding: const EdgeInsets.only(
              left: 16, right: 16, top: 4, bottom: 4),
          child: TextFormField(
            obscureText: true,
            onChanged: (String txt) {},
            style: const TextStyle(
              fontSize: 18,
            ),
            cursorColor: AppTheme.buildLightTheme().primaryColor,
            decoration: InputDecoration(
              border: InputBorder.none,
              labelText: 'Password',
              labelStyle: AppTheme.body1,          
              ),
            validator: (value) {
              if (value.isEmpty) {
                return 'Please enter Password';
              }
              return null;
            },
            keyboardType: TextInputType.visiblePassword,

            onSaved: (value)=>_password=value,
          ),

        ),
      ),
    );
  }

  Widget _getUserIdField(BuildContext context){
    return Padding(
      padding: const EdgeInsets.only(
              left: 16, right: 16, top: 4, bottom: 4),
      child:Container(
        decoration: BoxDecoration(
          color: AppTheme.buildLightTheme().backgroundColor,
          borderRadius: const BorderRadius.all(
            Radius.circular(38.0),
          ),
          boxShadow: <BoxShadow>[
            BoxShadow(
                color: Colors.grey.withOpacity(0.2),
                offset: const Offset(0, 2),
                blurRadius: 8.0),
          ],
        ),
        child: Padding(
          padding: const EdgeInsets.only(
              left: 16, right: 16, top: 4, bottom: 4),
          child: TextFormField(
            onChanged: (String txt) {},
            style: const TextStyle(
              fontSize: 18,
            ),
            cursorColor: AppTheme.buildLightTheme().primaryColor,
            decoration: InputDecoration(
              border: InputBorder.none,
              labelText: 'User Id',
              labelStyle: AppTheme.body1,
            ),
            keyboardType: TextInputType.emailAddress,
            validator: (value) {
              if (value.isEmpty) {
                return 'Please enter user id';
              }
              return null;
            },
            onSaved: (value)=>_email=value,
          ),
        ),
      ),
    );
  }

  Widget _getLoginButton(BuildContext context){
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: Container(
        decoration: BoxDecoration(
          color: AppTheme.buildLightTheme().primaryColor,
          borderRadius: const BorderRadius.all(
            Radius.circular(38.0),
          ),
          boxShadow: <BoxShadow>[
            BoxShadow(
                color: Colors.grey.withOpacity(0.4),
                offset: const Offset(0, 2),
                blurRadius: 8.0),
          ],
        ),
        child: Material(
          color: Colors.transparent,
          child: InkWell(
            borderRadius: const BorderRadius.all(
              Radius.circular(32.0),
            ),
            onTap: () {
              if (_formKey.currentState.validate()) {

               _onLoginButtonPressed();
              }
                         
            },
            child: Padding(
              padding: const EdgeInsets.only(right:70.0,left:70.0,top: 16.0,bottom: 16.0),
              child: Text(
                'Login',
                style: AppTheme.buttonText,
              )
            ),
          ),
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
