class TestCase:
    def __init__(self, case_id, description, do_test, setup = None):
        """
        :param case_id: The test number
        :type case_id: Number
        :param description: Description of the test
        :type description: String
        :param do_test: Function that evaluates the test and return True or False
        :type do_test: Function 
        :param setup: Optional preliminary function which can be used to setup 
                      the robot before the test has been run
        :type setup: Function
        """
     
        self.case_id = case_id
        self.description = description
        self.do_test = do_test
        self.setup = setup
        self.result = None

    def get_csv(self):
        """ Returns csv of test_case

        :return str: A csv of the test_case
        :type str: string
        """
        return ','.join([
            str(self.case_id),
            str(self.description),
            str(self.result)
        ])
