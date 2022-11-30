# Generated by Django 4.1.2 on 2022-11-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('D', 'Em dia'), ('A', 'Em atraso')], default='D', max_length=1, verbose_name='Status')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor do empréstimo')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('juros', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Juros')),
                ('parcelas', models.SmallIntegerField()),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.conta', verbose_name='Conta')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_transacao', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('valor_transacao', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('beneficiado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiado', to='bank.conta', verbose_name='Beneficiado')),
                ('beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiario', to='bank.conta', verbose_name='Beneficiário')),
            ],
        ),
        migrations.CreateModel(
            name='Pag_emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateField(verbose_name='Data de vencimento')),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor da parcela')),
                ('data_pagamento', models.DateField(verbose_name='Data de pagamento')),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.emprestimo', verbose_name='Emprestimo')),
            ],
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctt_favorito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorito', to='bank.usuario', verbose_name='Favorito')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='bank.usuario', verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_fatura', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_vencimento', models.DateField(verbose_name='Vencimento')),
                ('data_pagamento', models.DateField(verbose_name='Pagamento')),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.cartao', verbose_name='Cartão')),
            ],
        ),
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operacao', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], default='E', max_length=1, verbose_name='Operação')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.conta', verbose_name='Conta')),
            ],
        ),
    ]