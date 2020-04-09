
import 'package:flutter/material.dart';
import 'package:sams/models/user.dart';
import 'package:sams/screens/common/home_screen.dart';
import 'package:sams/screens/login/forget_password.dart';
import 'package:sams/screens/root/navigation_home_screen.dart';
import 'package:sams/theme/app_theme.dart';

import 'login_screen_presenter.dart';

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> implements LoginScreenContract{

  bool _isLoading=false;
  LoginScreenPresenter _presenter;
  final scaffoldKey = new GlobalKey<ScaffoldState>();
  final formKey = new GlobalKey<FormState>();
  String _username,_password;


  _LoginScreenState() {
    _presenter = new LoginScreenPresenter(this);
    // var authStateProvider = new AuthStateProvider();
    // authStateProvider.subscribe(this);
  }

  void _submit() {
    final form = formKey.currentState;

    if (form.validate()) {
      setState(() => _isLoading = true);
      form.save();
      _presenter.doLogin(_username, _password);
    }
  }

  void _showSnackBar(String text) {
    scaffoldKey.currentState
        .showSnackBar(new SnackBar(content: new Text(text)));
  }

  @override
  void onLoginError(String errorTxt) {
    _showSnackBar(errorTxt);
    setState(() => _isLoading = false);
  }

  @override
  void onLoginSuccess(User user) async {
    _showSnackBar('Successful'+user.toString());
    setState(() => _isLoading = false);
    Navigator.push(context, MaterialPageRoute(builder: (context)=>NavigationHomeScreen()));

    // var db = new DatabaseHelper();
    // await db.saveUser(user);
    // var authStateProvider = new AuthStateProvider();
    // authStateProvider.notify(AuthState.LOGGED_IN);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      // appBar: AppBar(
      //   backgroundColor: Colors.transparent,
      //   elevation: 0.0,
        
      // ),
      body: Container(
        width: double.infinity,
        child: Form(
          key: formKey,
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.only(top :100.0,right: 40,left:40,bottom:100),
                  child: Image.asset('assets/logo.png'),
                  ),
                _getUserIdField(context),
                _getPasswordField(context),
                _getLoginButton(context),  
                _getForgetButton(context),
                ],
            ),
          ),
        ),
      )
    );
  }

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
            onSaved: (value)=>_username=value,
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
              _submit();
              // FocusScope.of(context).requestFocus(FocusNode());
              // Navigator.push(context, MaterialPageRoute(builder: (context)=>NavigationHomeScreen()));
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
