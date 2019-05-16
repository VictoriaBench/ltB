import unittest
import find_exams

class TestStringMethods(unittest.TestCase):

    def test_getCoursesForLects(self):
        fname = 'lectlist.csv'
        ans1 = find_exams.getCoursesForLects(fname)
        self.assertEqual(ans1,{ 'Levitt': ['ELEN4010', 'ELEN3008'], 'Hazelhurst': ['ELEN7039', 'ELEN3020', 'COMS7059'], 'Hofsajer': ['ELEN3003', 'ELEN3002'], 'Dinger': ['SCMD1003'], 'Cronje': ['ELEN4014']})

    def test_getExams(self):
        fname = 'examlist.csv'
        ans1 = find_exams.getExams(fname)
        self.assertEqual(ans1, {'ELEN3003': ('2020-05-24', 'CM3'), 'ELEN3002': ('2020-05-24', 'CM3'), 'ELEN7039': ('2020-06-15', 'CM2'), 'SCMD1003': ('2020-05-28', 'CM2'), 'ELEN4013': ('2020-06-01', 'SHWWB'), 'ELEN3008': ('2020-06-03', 'EH'), 'COMS7059': ('2020-05-23', 'FNB64'), 'ELEN4010': ('2020-05-29', 'TND')})

    def test_getTimeTable(self):
        courses = { 'Levitt': ['ELEN4010', 'ELEN3008'], 'Hazelhurst': ['ELEN7039', 'ELEN3020', 'COMS7059'], 'Hofsajer': ['ELEN3003', 'ELEN3002'], 'Dinger': ['SCMD1003'], 'Cronje': ['ELEN4014']}
        exams = {'ELEN3003': ('2020-05-24', 'CM3'), 'ELEN3002': ('2020-05-24', 'CM3'), 'ELEN7039': ('2020-06-15', 'CM2'), 'SCMD1003': ('2020-05-28', 'CM2'), 'ELEN4013': ('2020-06-01', 'SHWWB'), 'ELEN3008': ('2020-06-03', 'EH'), 'COMS7059': ('2020-05-23', 'FNB64'), 'ELEN4010': ('2020-05-29', 'TND')}
        ans = find_exams.getTimeTable(courses, exams)
        self.assertEqual(ans, [('Cronje', [('ELEN4014', ('TBD', 'TBD'))]), ('Dinger', [('SCMD1003', ('2020-05-28', 'CM2'))]), ('Hazelhurst', [('ELEN7039', ('2020-06-15', 'CM2')), ('ELEN3020', ('TBD', 'TBD')), ('COMS7059', ('2020-05-23', 'FNB64'))]), ('Hofsajer', [('ELEN3003', ('2020-05-24', 'CM3')), ('ELEN3002', ('2020-05-24', 'CM3'))]), ('Levitt', [('ELEN4010', ('2020-05-29', 'TND')), ('ELEN3008', ('2020-06-03', 'EH'))])])

    #def test_getExams(self):	


if __name__ == '__main__':
    unittest.main()


