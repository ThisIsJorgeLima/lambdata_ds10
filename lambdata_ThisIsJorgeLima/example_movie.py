class Movie: 
  """
  This is an abstract a movie structure
  """

  def __init__(self, leading_actor='Leonardo DiCaprio',
              supporting_actor='Brad Pitt',
              run_time=130):
   
   self.leading_actor = leading_actor
   self.supporting_actor = supporting_actor
   self.run_time = run_time

  def who_is_leading(self):
    """

    Who is the star of the film
    """
    print('The leading star is {}'.format(self.leading_actor))
  
  def who_is_supporting(self):

    """
    Who is the supporting actor?
    """
    print('The supporting actor is {}'.format(self.supporting_actor))

  def what_is_run_time(self):

    """
    What is the running time?
    """
    print('The running time is {}'.format(self.run_time))