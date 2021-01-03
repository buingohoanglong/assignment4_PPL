.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is k I from Label0 to Label1
	iconst_0
	istore_3
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 12
	iastore
	dup
	iconst_1
	bipush 11
	iastore
	dup
	iconst_2
	bipush 10
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 7
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 6
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	iconst_4
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_1
	iastore
	aastore
	aastore
	astore 4
Label0:
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	iconst_0
	istore_2
Label10:
	iload_2
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label8:
	iconst_0
	istore_3
Label16:
	iload_3
	iconst_3
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label17
Label14:
	aload 4
	iload_1
	aaload
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label15:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label16
Label17:
Label9:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label10
Label11:
Label3:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label5:
	invokestatic io/printLn()V
	aload 4
	invokestatic MCClass/foo([[[I)V
	iconst_0
	istore_1
Label22:
	iload_1
	iconst_2
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label23
Label20:
	iconst_0
	istore_2
Label28:
	iload_2
	iconst_2
	if_icmpge Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifle Label29
Label26:
	iconst_0
	istore_3
Label34:
	iload_3
	iconst_3
	if_icmpge Label36
	iconst_1
	goto Label37
Label36:
	iconst_0
Label37:
	ifle Label35
Label32:
	aload 4
	iload_1
	aaload
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label33:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label34
Label35:
Label27:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label28
Label29:
Label21:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label22
Label23:
Label1:
	return
.limit stack 47
.limit locals 5
.end method

.method public static foo([[[I)V
.var 0 is x [[[I from Label0 to Label1
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 11
	iastore
	dup
	iconst_2
	bipush 12
	iastore
	aastore
	aastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is k I from Label0 to Label1
	iconst_0
	istore 4
Label0:
	aload_0
	astore_1
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	iconst_0
	istore_3
Label10:
	iload_3
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label8:
	iconst_0
	istore 4
Label16:
	iload 4
	iconst_3
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label17
Label14:
	aload_1
	iload_2
	aaload
	iload_3
	aaload
	iload 4
	iload_2
	iload_3
	iadd
	iload 4
	iadd
	iastore
Label15:
	iconst_1
	iload 4
	iadd
	istore 4
	goto Label16
Label17:
Label9:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label10
Label11:
Label3:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label4
Label5:
Label1:
	return
.limit stack 32
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
