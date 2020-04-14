import 'package:flutter/material.dart';
import 'package:sams/screens/root/navigation_home_screen.dart';
import 'package:sams/theme/app_theme.dart';

class SetPassword extends StatefulWidget {
  @override
  _SetPasswordState createState() => _SetPasswordState();
}

class _SetPasswordState extends State<SetPassword> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
      // appBar: AppBar(
      //   backgroundColor: Colors.transparent,
      //   elevation: 0.0,
      // ),
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
              _getNewPasswordField(context),
              _getConfirmPasswordField(context), 
              _getConfirmButton(context),
              ],
          ),
        ),
      )
    );
  }
}

Widget _getNewPasswordField(BuildContext context){
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
        child: TextField(
          obscureText: true,
          onChanged: (String txt) {},
          style: const TextStyle(
            fontSize: 18,
          ),
          cursorColor: AppTheme.buildLightTheme().primaryColor,
          decoration: InputDecoration(
            border: InputBorder.none,
            labelText: 'New Password',
            labelStyle: AppTheme.body1,          ),
        ),
      ),
    ),
  );
}

Widget _getConfirmPasswordField(BuildContext context){
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
              labelText: 'Confirm Password',
              labelStyle: AppTheme.body1,
              border: InputBorder.none,
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
            // FocusScope.of(context).requestFocus(FocusNode());
            Navigator.push(context, MaterialPageRoute(builder: (context)=>NavigationHomeScreen()));
          },
          child: Padding(
            padding: const EdgeInsets.only(right:70.0,left:70.0,top: 16.0,bottom: 16.0),
            child: Text(
              'Confirm',
              style: AppTheme.buttonText,
            )
          ),
        ),
      ),
    ),
  );
}
