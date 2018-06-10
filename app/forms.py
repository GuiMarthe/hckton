from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    professor_name = StringField('Nome do Responsável', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    project_description = TextAreaField('Descrição do Projeto', validators=[DataRequired()])
    key_words = StringField('Palavras Chave', validators=[DataRequired()])
    project_title = StringField('Titulo do projeto', validators=[DataRequired()])
    submit = SubmitField('Adicionar projeto')


class ProfessorSearch(FlaskForm):
    search = StringField('Busca professores')
    submit = SubmitField('Buscar')
