import 'dart:async';
import 'dart:developer';

import 'package:meta/meta.dart';
import 'package:bloc/bloc.dart';
import 'package:sams/blocs/course/course_info_event.dart';
import 'package:sams/blocs/course/course_info_state.dart';
import 'package:sams/models/course_info.dart';
import 'package:sams/services/rest_ds.dart';


class CourseInfoBloc extends Bloc<CourseInfoEvent, CourseInfoState> {
  final String courseCode;
  final RestDatasource api=RestDatasource();

  CourseInfoBloc({@required this.courseCode});

  CourseInfoState get initialState => CourseInfoInitial();

    @override
    Stream<CourseInfoState> mapEventToState( CourseInfoEvent event,) async* {

      if (event is CourseInfoInitiate) {
        //TODO: Implement getting data from cache memory 
        yield CourseInfoLoading();
        try{
          CourseInfo courseInfo=await api.getCourseInfo(courseCode);
          await Future<dynamic>.delayed(const Duration(milliseconds: 1000));
          yield CourseInfoSuccess(courseInfo: courseInfo);
        }
        catch(error){
          log(error.toString());
          yield CourseInfoFailure(error: error);
        }
      }
    }
}
