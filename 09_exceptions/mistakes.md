except (ValueError, IndexError):
    if ValueError:
        ...
    if IndexError:
        ...

no se toma asi, seria asi:

except ValueError:
    ...

except IndexError:
    ...

Capturar Exception demasiado pronto

try:
    ...
except Exception:
    print("Something failed")

funciona pero es demasiado rapido, oculta informacion importante

es mejor except ValueError:

except: desnudo

try:
    ...
except:
    ...

captura prácticamente cualquier cosa y puede esconder errores que deberías conocer.

Capturar y no hacer nada

try:
    ...
except ValueError:
    pass

puede hacer desaparecer un problema silenciosamente.