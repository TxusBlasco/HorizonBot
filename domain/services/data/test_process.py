import unittest
import pandas as pd
import process
from pandas.testing import assert_frame_equal

last_df = pd.DataFrame([
	{'title': 'Permanently Open Call for Targeted Innovation Projects', 'id': 'EITUM-BP23-25',
	 'funding_type': 'Cascade '
	                 'funding', 'program': 'Horizon Europe (HORIZON)',
	 'status': 'Open for submission', 'grant_or_tender': 'Grant',
	 'topic': 'HORIZON-EIT-2023-25-KIC-EITURBANMOBILITY', 'deadline_model': 'multiple cut-off',
	 'opening_date': '14 December 2023', 'closing_date': '31 December 2025 17:00:00 Brussels time'},
	{
		'title': 'Identification or Validation of Targets for Personalised Medicine Approaches ('
		         'PMTargets)',
		'id': 'EP PerMed', 'funding_type': 'Cascade funding', 'program': 'Horizon Europe (HORIZON)',
		'status': 'Open for submission', 'grant_or_tender': 'Grant',
		'topic': 'HORIZON-HLTH-2023-CARE-08-01', 'deadline_model': 'single-stage',
		'opening_date': '02 January 2024', 'closing_date': '5 March 2024 17:00:00 Brussels time'},
	{
		'title': 'Gaining experience and confidence in New Approach Methodologies (NAM) for '
		         'regulatory safety and efficacy'
		         'testing – coordinated training and experience exchange for regulators',
		'id': 'HORIZON-HLTH-2024-IND-06-09', 'funding_type': 'Call for proposal',
		'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
		'grant_or_tender': 'Grant', 'topic': 'HORIZON Coordination and Support Actions',
		'deadline_model': 'single-stage', 'opening_date': '26 October 2023',
		'closing_date': '11 April 2024 17:00:00 Brussels time'},
	{'title': 'Improving clinical management of heart disease from early detection to treatment',
	 'id': 'HORIZON-JU-IHI-2024-07-01-singe-stage', 'funding_type': 'Call for proposal',
	 'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
	 'grant_or_tender': 'Grant', 'topic': 'HORIZON JU Research and Innovation Actions',
	 'deadline_model': 'single-stage', 'opening_date': '16 January 2024',
	 'closing_date': '22 May 2024 17:00:00 Brussels time'},
	{
		'title': 'Next generation low-emission, climate-resilient pathways and NDCs for a future '
		         'aligned with the Paris'
		         'Agreement', 'id': 'HORIZON-CL5-2024-D1-01-05',
		'funding_type': 'Call for proposal', 'program': 'Horizon Europe (HORIZON)',
		'status': 'Open for submission', 'grant_or_tender': 'Grant',
		'topic': 'HORIZON Research and Innovation Actions', 'deadline_model': 'single-stage',
		'opening_date': '12 September 2023', 'closing_date': '5 March 2024 17:00:00 Brussels time'},
	{
		'title': 'Novel paradigms and approaches, towards AI-powered robots– step change in '
		         'functionality (AI,'
		         'data and robotics partnership) (RIA)',
		'id': 'HORIZON-CL4-2024-DIGITAL-EMERGING-01-03', 'funding_type': 'Call for proposal',
		'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
		'grant_or_tender': 'Grant', 'topic': 'HORIZON Research and Innovation Actions',
		'deadline_model': 'single-stage', 'opening_date': '15 November 2023',
		'closing_date': '19 March 2024 17:00:00 Brussels time'},
	{
		'title': 'Smart photonics for joint communication & sensing and access everywhere ('
		         'Photonics Partnership) (RIA)',
		'id': 'HORIZON-CL4-2024-DIGITAL-EMERGING-01-54', 'funding_type': 'Call for proposal',
		'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
		'grant_or_tender': 'Grant', 'topic': 'HORIZON Research and Innovation Actions',
		'deadline_model': 'single-stage', 'opening_date': '15 November 2023',
		'closing_date': '19 March 2024 17:00:00 Brussels time'},
	{'title': 'Modulation of brain ageing through nutrition and healthy lifestyle (NutriBrain)',
	 'id': 'ERA4Health',
	 'funding_type': 'Cascade funding', 'program': 'Horizon Europe (HORIZON)',
	 'status': 'Open for submission', 'grant_or_tender': 'Grant',
	 'topic': 'HORIZON-HLTH-2022-DISEASE-03-01', 'deadline_model': 'multiple cut-off',
	 'opening_date': '03 November 2023', 'closing_date': '27 May 2024 17:00:00 Brussels time'},
	{'title': 'Nano and advanced technologies for disease prevention, diagnostic and therapy',
	 'id': 'ERA4Health',
	 'funding_type': 'Cascade funding', 'program': 'Horizon Europe (HORIZON)',
	 'status': 'Open for submission', 'grant_or_tender': 'Grant',
	 'topic': 'HORIZON-HLTH-2022-DISEASE-03-01', 'deadline_model': 'multiple cut-off',
	 'opening_date': '14 November 2023', 'closing_date': '13 June 2024 17:00:00 Brussels time'}])

new_df = pd.DataFrame([
	{'title': 'Strategic Business Alliance for Urban Mobility – E&S Permanently Open call',
                        'id': 'EITUM-BP23-25',
                        'funding_type': 'Cascade funding', 'program': 'Horizon Europe (HORIZON)',
                        'status': 'Open for submission', 'grant_or_tender': 'Grant',
                        'topic': 'HORIZON-EIT-2023-25-KIC-EITURBANMOBILITY', 'deadline_model': 'multiple cut-off',
                        'opening_date': '20 October 2023', 'closing_date': '20 May 2024 17:00:00 Brussels time'},
                       {'title': 'Permanently Open Call for Targeted Innovation Projects', 'id': 'EITUM-BP23-25',
                        'funding_type': 'Cascade '
                                        'funding', 'program': 'Horizon Europe (HORIZON)',
                        'status': 'Open for submission', 'grant_or_tender': 'Grant',
                        'topic': 'HORIZON-EIT-2023-25-KIC-EITURBANMOBILITY', 'deadline_model': 'multiple cut-off',
                        'opening_date': '14 December 2023', 'closing_date': '31 December 2025 17:00:00 Brussels time'},
                       {
	                       'title': 'Identification or Validation of Targets for Personalised Medicine Approaches ('
	                                'PMTargets)',
	                       'id': 'EP PerMed', 'funding_type': 'Cascade funding', 'program': 'Horizon Europe (HORIZON)',
	                       'status': 'Open for submission', 'grant_or_tender': 'Grant',
	                       'topic': 'HORIZON-HLTH-2023-CARE-08-01', 'deadline_model': 'single-stage',
	                       'opening_date': '02 January 2024', 'closing_date': '5 March 2024 17:00:00 Brussels time'},
                       {
	                       'title': 'Gaining experience and confidence in New Approach Methodologies (NAM) for '
	                                'regulatory safety and efficacy'
	                                'testing – coordinated training and experience exchange for regulators',
	                       'id': 'HORIZON-HLTH-2024-IND-06-09', 'funding_type': 'Call for proposal',
	                       'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
	                       'grant_or_tender': 'Grant', 'topic': 'HORIZON Coordination and Support Actions',
	                       'deadline_model': 'single-stage', 'opening_date': '26 October 2023',
	                       'closing_date': '11 April 2024 17:00:00 Brussels time'},
                       {'title': 'Improving clinical management of heart disease from early detection to treatment',
                        'id': 'HORIZON-JU-IHI-2024-07-01-singe-stage', 'funding_type': 'Call for proposal',
                        'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
                        'grant_or_tender': 'Grant', 'topic': 'HORIZON JU Research and Innovation Actions',
                        'deadline_model': 'single-stage', 'opening_date': '16 January 2024',
                        'closing_date': '22 May 2024 17:00:00 Brussels time'},
                       {
	                       'title': 'Next generation low-emission, climate-resilient pathways and NDCs for a future '
	                                'aligned with the Paris'
	                                'Agreement', 'id': 'HORIZON-CL5-2024-D1-01-05',
	                       'funding_type': 'Call for proposal', 'program': 'Horizon Europe (HORIZON)',
	                       'status': 'Open for submission', 'grant_or_tender': 'Grant',
	                       'topic': 'HORIZON Research and Innovation Actions', 'deadline_model': 'single-stage',
	                       'opening_date': '12 September 2023', 'closing_date': '5 March 2024 17:00:00 Brussels time'},
                       {
	                       'title': 'Novel paradigms and approaches, towards AI-powered robots– step change in '
	                                'functionality (AI,'
	                                'data and robotics partnership) (RIA)',
	                       'id': 'HORIZON-CL4-2024-DIGITAL-EMERGING-01-03', 'funding_type': 'Call for proposal',
	                       'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
	                       'grant_or_tender': 'Grant', 'topic': 'HORIZON Research and Innovation Actions',
	                       'deadline_model': 'single-stage', 'opening_date': '15 November 2023',
	                       'closing_date': '19 March 2024 17:00:00 Brussels time'},
                       {
	                       'title': 'Smart photonics for joint communication & sensing and access everywhere ('
	                                'Photonics Partnership) (RIA)',
	                       'id': 'HORIZON-CL4-2024-DIGITAL-EMERGING-01-54', 'funding_type': 'Call for proposal',
	                       'program': 'Horizon Europe (HORIZON)', 'status': 'Open for submission',
	                       'grant_or_tender': 'Grant', 'topic': 'HORIZON Research and Innovation Actions',
	                       'deadline_model': 'single-stage', 'opening_date': '15 November 2023',
	                       'closing_date': '19 March 2024 17:00:00 Brussels time'},
                       {
	                       'title': 'Modulation of brain ageing through nutrition and healthy lifestyle (NutriBrain)',
	                       'id': 'ERA4Health',
	                       'funding_type': 'Cascade funding', 'program': 'Horizon Europe (HORIZON)',
	                       'status': 'Open for submission', 'grant_or_tender': 'Grant',
	                       'topic': 'HORIZON-HLTH-2022-DISEASE-03-01', 'deadline_model': 'multiple cut-off',
	                       'opening_date': '03 November 2023', 'closing_date': '27 May 2024 17:00:00 Brussels time'}])


class TestProcess(unittest.TestCase):
	def test_compare_df(self):
		actual = process.compare_df(last_df, new_df)
		expected = {
				'deleted': pd.DataFrame(
					{
						'title': 'Nano and advanced technologies for disease prevention, diagnostic and therapy',
						'id': 'ERA4Health',
						'funding_type': 'Cascade funding',
						'program': 'Horizon Europe (HORIZON)',
						'status': 'Open for submission',
						'grant_or_tender': 'Grant',
						'topic': 'HORIZON-HLTH-2022-DISEASE-03-01',
						'deadline_model': 'multiple cut-off',
						'opening_date': '14 November 2023',
						'closing_date': '13 June 2024 17:00:00 Brussels time'
					}, index=[4]
				),
				'added': pd.DataFrame(
					{
						'title': 'Strategic Business Alliance for Urban Mobility – E&S Permanently Open call',
						'id': 'EITUM-BP23-25',
						'funding_type': 'Cascade funding',
						'program': 'Horizon Europe (HORIZON)',
						'status': 'Open for submission',
						'grant_or_tender': 'Grant',
						'topic': 'HORIZON-EIT-2023-25-KIC-EITURBANMOBILITY',
						'deadline_model': 'multiple cut-off',
						'opening_date': '20 October 2023',
						'closing_date': '20 May 2024 17:00:00 Brussels time'
					}, index=[9]
				)
			}
		for key in expected.keys():
			assert_frame_equal(actual[key], expected[key])


if __name__ == '__main__':
	unittest.main()
