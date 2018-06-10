from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class addProjectForm(FlaskForm):
    professor_name = StringField('Nome do Responsável', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    project_description = StringField('Descrição do Projeto', validators=[DataRequired()])
    key_words = StringField('Palavras Chave', validators=[DataRequired()])
    project_title = StringField('Titulo do projeto', validators=[DataRequired()])
    submit = SubmitField('Adicionar projeto')
