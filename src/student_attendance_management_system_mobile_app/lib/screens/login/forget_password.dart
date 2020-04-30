import 'package:flutter/material.dart';
import 'package:sams/screens/login/set_password.dart';
import 'package:sams/theme/app_theme.dart';

class ForgetPassword extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: null,
      body: Container(
        width: double.infinity,
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Padding(
                padding: EdgeInsets.only(top :100.0,right: 40,left:40,bottom:100),
                child: Image.asset('assets/logo.png'),
                ),
              Padding(
                padding: EdgeInsets.only(top:40.0),
                child: Text(
                  'Please Enter User Id',
                  style: AppTheme.headline,
                  ),
                ),
              _getUserIdField(context),
              _getConfirmButton(context), 
              ],
          ),
        ),
      )
    );
  }

Widget _getUserIdField(BuildContext context){
  return Padding(
    padding: const EdgeInsets.only(
            left: 16, right: 16, top: 10, bottom: 4),
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
        child: TextField(
          onChanged: (String txt) {},
          style: const TextStyle(
            fontSize: 18,
          ),
          cursorColor: AppTheme.buildLightTheme().primaryColor,
          decoration: InputDecoration(
            border: InputBorder.none,
            labelText: 'User ID',
            labelStyle: AppTheme.body1,
          ),
        ),
      ),
    ),
  );
}

Widget _getConfirmButton(BuildContext context){
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
            FocusScope.of(context).requestFocus(FocusNode());
            Navigator.push(context, MaterialPageRoute(builder: (context)=> new SetPassword()));
          },
          child: Padding(
            padding: const EdgeInsets.only(right:70.0,left:70.0,top: 16.0,bottom: 16.0),
            child: Text(
              'Confirm',
              style: AppTheme.buttonText,
            ),
          )
        ),
      ),
    ),
  );

  }
}

