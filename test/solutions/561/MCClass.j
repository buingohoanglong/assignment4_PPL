.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_5
	newarray float
	dup
	iconst_0
	ldc 1.1
	fastore
	dup
	iconst_1
	ldc 2.2
	fastore
	dup
	iconst_2
	ldc 3.3
	fastore
	dup
	iconst_3
	ldc 4.4
	fastore
	dup
	iconst_4
	ldc 5.5
	fastore
	putstatic MCClass/x [F
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	getstatic MCClass/x [F
	iload_1
	getstatic MCClass/x [F
	iload_1
	faload
	iconst_2
	invokestatic io/float_to_int(I)F
	fmul
	ldc 1.0
	fadd
	fastore
Label3:
Label4:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label2
Label5:
	iconst_0
	istore_1
Label8:
	iload_1
	iconst_5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	getstatic MCClass/x [F
	iload_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label9:
Label10:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label8
Label11:
Label1:
	return
.limit stack 20
.limit locals 2
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
