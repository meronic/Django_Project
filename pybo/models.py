from django.db import models


class Question(models.Model) : 
    
    objects = models.Manager() # object 경고 에러 수정
    
    
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self) : 
        return self.subject
    
    
        
    
class Answer(models.Model) : 
    question = models.ForeignKey(Question, on_delete = models.CASCADE) 
    # ForeignKey > 다른모델과의 연결의 의미 여기서는 위의 Question과의 연결을 의미한다
    # on_delete = models.CASCADE > 답변과 연결된 질문이 삭제 되면 답변도 같이 삭제를 의미
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self) : 
        return self.question
    
