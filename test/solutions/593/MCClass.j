.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	dup
	iconst_2
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 6
	iastore
	aastore
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label0:
Label4:
	iload_2
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
.var 3 is j I from Label2 to Label3
	iconst_0
	istore_3
Label2:
	iload_2
	iload_3
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
Label12:
	goto Label4
Label13:
	goto Label9
Label8:
Label14:
Label15:
Label9:
Label18:
	iload_3
	iconst_2
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label19
Label16:
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	iconst_3
	if_icmpne Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label22
Label26:
	goto Label18
Label27:
	goto Label23
Label22:
Label28:
Label29:
Label23:
Label17:
	goto Label18
Label19:
	iload_2
	iconst_1
	iadd
	istore_2
Label3:
	goto Label4
Label5:
	return
Label1:
	return
	return
.limit stack 23
.limit locals 4
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
