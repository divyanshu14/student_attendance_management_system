import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:sams/blocs/login/login_bloc.dart';
import 'package:sams/blocs/login/login_events.dart';
import 'package:sams/blocs/login/login_state.dart';
import 'package:sams/theme/app_theme.dart';


class LoginForm extends StatefulWidget {
  @override
  _LoginFormState createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {

  final _formKey = new GlobalKey<FormState>();
  String _email,_password;
  String initialPassword ='new_pass_123';
  String initialUserId='2017csb1062@iitrpr.ac.in';

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
            initialValue: initialPassword,
            obscureText: true,
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
            initialValue: initialUserId,
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
}
