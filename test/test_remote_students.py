from src.remote_students import added_remote_location
"""This function must be a PURE FUNCTION, 
i.e. it should have no side effects. 
Your test suite should reflect this."""


# test setup 

 


class TestBuildOfRemoteStudents():
    def test_setup_of_files(self):
        assert added_remote_location

    def test_call_one_dict_student(self):
        input_data = [
            { "name": 'Euler', "age": 27 }
        ]
        excepted_data = [
            { "name": 'Euler', "age": 27, "location": 'remote'}
        ]

        output = added_remote_location(input_data)

        assert output == excepted_data

    def test_call_multiple_student_dict(self):
        input_data = [
            { "name": 'Hypatia', "age": 31, "location": 'leeds' },
            { "name": 'Ramanujan', "age": 22 },
            { "name": 'Tao', "age": 47, "location": 'manchester' }
        ]
        expected_data = [
            { "name": 'Hypatia', "age": 31, "location": 'leeds' },
            { "name": 'Ramanujan', "age": 22, "location": 'remote' },
            { "name": 'Tao', "age": 47, "location": 'manchester' }
        ]
        output = added_remote_location(input_data)

        assert output == expected_data

class TestPureFunctionOfRemoteStudents():
    def test_call_dict_not_modified(self):
        input_data = [
            { "name": 'Euler', "age": 27 }
        ]
        output_data = added_remote_location(input_data)
        assert output_data != input_data
    
    def test_call_dict_no_other_changes(self):
        input_data = [
            { "name": 'Euler', "age": 27 }
        ]
        failed_test = [
            { "name": 'Euler', "age": 27, "payment": 'private' }
        ]
        output_data = added_remote_location(input_data)
        assert output_data != failed_test
