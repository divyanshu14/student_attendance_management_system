
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:sams/theme/app_theme.dart';
import 'package:sams/ui/custom_drawer/calendar/calendar_popup_view.dart';

class DailyAttendance extends StatefulWidget {
  @override
  _DailyAttendanceState createState() => _DailyAttendanceState();
}

class _DailyAttendanceState extends State<DailyAttendance> {

  DateTime currentDate = DateTime.now();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
      appBar: _appBar(context),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[  
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.all(10.0),
                        child: Container(
                          decoration: BoxDecoration(
                            color: AppTheme.buildLightTheme().primaryColor,
                            borderRadius: BorderRadius.circular(40),
                            boxShadow: <BoxShadow>[
                              BoxShadow(
                                  color: AppTheme.grey.withOpacity(0.2),
                                  offset: Offset(1.1, 1.1),
                                  blurRadius: 10.0),
                            ]
                          ),
                          child: InkWell(
                            focusColor: Colors.transparent,
                            highlightColor: Colors.transparent,
                            hoverColor: Colors.transparent,
                            splashColor: Colors.grey.withOpacity(0.2),
                            borderRadius: const BorderRadius.all(
                              Radius.circular(4.0),
                            ),
                            onTap: () {
                              FocusScope.of(context).requestFocus(FocusNode());
                              // setState(() {
                              //   isDatePopupOpen = true;
                              // });
                              _calendarDialog(context: context);
                            },
                            child: Center(
                              child: Padding(
                                padding: const EdgeInsets.only(
                                     top: 20, bottom: 20),
                                child: 
                                    Text(
                                      '${DateFormat("dd, MMM").format(currentDate)}',
                                      style: AppTheme.headlineLight
                                    ),
                              ),
                            ),
                          ),
                        ),
                      ),
                    ),
                  ]
                ),
        _attendanceSummary(),
        _studentsList(),
        ],
      ),
    );
  }
  Widget _appBar(context){
    return AppBar(
      leading: SizedBox(
        width: AppBar().preferredSize.height,
        height: AppBar().preferredSize.height,
        child: InkWell(
          borderRadius:
              BorderRadius.circular(AppBar().preferredSize.height),
          child: Icon(
            Icons.arrow_back_ios,
            color: AppTheme.buildLightTheme().iconTheme.color,
          ),
          onTap: () {
            Navigator.pop(context);
          },
        ),
      ),
      title: Text('Daily Attendance',
        style: AppTheme.headline,
      ),
      centerTitle: true,
      backgroundColor: AppTheme.buildLightTheme().scaffoldBackgroundColor,
      elevation: 0.0,
    );
  }

  void _calendarDialog({BuildContext context}) {
    showDialog<dynamic>(
      context: context,
      builder: (BuildContext context) => CalendarPopupView(
        barrierDismissible: true,
        // minimumDate: DateTime.now(),
         maximumDate: DateTime.now(),
        initialEndDate: currentDate,
        initialStartDate: null,
        onApplyClick: (DateTime startData, DateTime endData) {
          setState(() {
            if (startData != null && endData != null) {
              currentDate = startData;
            }
          });
        },
        onCancelClick: () {},
      ),
    );
  }

  Widget _attendanceSummary(){
    return Padding(
      padding: EdgeInsets.all(10),
      child: Container(
        decoration: BoxDecoration(
          color: AppTheme.white,
          borderRadius: BorderRadius.only(
              topLeft: Radius.circular(68.0),
              bottomLeft: Radius.circular(68.0),
              bottomRight: Radius.circular(68.0),
              topRight: Radius.circular(68.0)),
          boxShadow: <BoxShadow>[
            BoxShadow(
                color: AppTheme.grey.withOpacity(0.2),
                offset: Offset(1.1, 1.1),
                blurRadius: 10.0),
          ],
        ),
        child: Column(
          children: <Widget>[
            Padding(
              padding:
                  const EdgeInsets.only(top: 16, left: 16, right: 24),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Padding(
                    padding: const EdgeInsets.only(
                        left: 4, bottom: 0, top: 0),
                    child: Text(
                      'Attendance Summary',
                      textAlign: TextAlign.center,
                      style: AppTheme.body1),
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: <Widget>[
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: <Widget>[
                          Padding(
                            padding: const EdgeInsets.only(
                                left: 4, bottom: 8),
                            child: Text(
                              '90',
                              textAlign: TextAlign.center,
                              style: AppTheme.title
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.only(
                                left: 8, bottom: 8),
                            child: Text(
                              '%',
                              textAlign: TextAlign.center,
                              style: AppTheme.title
                            ),
                          ),
                        ],
                      ),
                      Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: <Widget>[
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: <Widget>[
                              Icon(
                                Icons.access_time,
                                color: AppTheme.grey
                                    .withOpacity(0.5),
                                size: 16,
                              ),
                              Padding(
                                padding:
                                    const EdgeInsets.only(left: 4.0),
                                child: Text(
                                  'Today 8:26 AM',
                                  textAlign: TextAlign.center,
                                  style: TextStyle(
                                    fontFamily:
                                        AppTheme.fontName,
                                    fontWeight: FontWeight.w500,
                                    fontSize: 14,
                                    letterSpacing: 0.0,
                                    color: AppTheme.grey
                                        .withOpacity(0.5),
                                  ),
                                ),
                              ),
                            ],
                          ),
                          Padding(
                            padding: const EdgeInsets.only(
                                top: 4, bottom: 14),
                            child: Text(
                              'Lecture',
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontFamily: AppTheme.fontName,
                                fontWeight: FontWeight.w500,
                                fontSize: 12,
                                letterSpacing: 0.0,
                                color: AppTheme.dark,
                              ),
                            ),
                          ),
                        ],
                      )
                    ],
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
                  
  }

  Widget _studentsList(){
    return Container(
      decoration: BoxDecoration(
            color: AppTheme.white,
            borderRadius: BorderRadius.only(
                topLeft: Radius.circular(68.0),
                bottomLeft: Radius.circular(68.0),
                bottomRight: Radius.circular(68.0),
                topRight: Radius.circular(68.0)),
            boxShadow: <BoxShadow>[
              BoxShadow(
                  color: AppTheme.grey.withOpacity(0.2),
                  offset: Offset(1.1, 1.1),
                  blurRadius: 10.0),
            ],
          ),
      child: Padding(
        padding: EdgeInsets.all(10),
        child: Text('No Students Yet')),
    );
  }

}